"""weblaze CLI"""

from pathlib import Path
import subprocess
import os
import sys
import yaml
from b2sdk.v2 import InMemoryAccountInfo, B2Api
from b2sdk.exception import InvalidAuthToken
import typer
import rich

from weblaze.utils import compress_files, upload_files, get_files


__version__ = "0.1.1"
app = typer.Typer()

CONFIG_DIR = Path.home() / f".config/{__package__}"
CONFIG_PATH = CONFIG_DIR / "config.yml"


def ensure_config_exists():
    """Ensure that the configuration file exists, or inform the user."""
    if not CONFIG_PATH.exists():
        # Option 1: Notify the user and exit
        rich.print(
            f":construction: Configuration file does not exist at: [blue]{CONFIG_PATH}[/blue]"
        )
        rich.print(
            ":bulb: You can run the [green]'init'[/green] command to generate a default configuration file."
        )
        rich.print(
            "Do you want to generate a default configuration now? [bold]y/n[/bold]"
        )
        choice = input()
        if choice == "y":
            init_config()
            rich.print(
                f"Created default configuration file at: [blue]{CONFIG_PATH}[/blue]"
            )
            edit_config()
            sys.exit(1)
        sys.exit(1)


def load_config():
    """load configuration"""
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


@app.command(name="init")
def init_config():
    """
    Initialize and generate a configuration file in the user's .config directory.
    """
    # Default configuration content
    config_content = """backblaze:
    application_key_id: YOUR_APPLICATION_KEY_ID
    application_key: YOUR_APPLICATION_KEY
    bucket_name: YOUR_BUCKET_NAME
local:
    compressor: PATH_TO_YOUR_COMPRESSOR"""

    # Ensure the .config/your_app directory exists
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    # Check if the configuration file already exists
    if CONFIG_PATH.exists():
        typer.echo(f"Configuration file already exists at: {CONFIG_PATH}")
        return

    # Create the configuration file with default settings
    try:
        CONFIG_PATH.write_text(config_content, encoding="utf-8")
        typer.echo(f"Configuration file created at: {CONFIG_PATH}")
    except Exception as e:
        typer.echo(f"Failed to create configuration file: {e}")


@app.command(name="edit")
def edit_config():
    """
    Edit the configuration file in the system's default editor.
    """
    try:
        if os.name == "posix":
            # For Unix-like systems, use $EDITOR if set, otherwise default to 'nano'
            editor = os.getenv("EDITOR", "nano")
            subprocess.run([editor, str(CONFIG_PATH)], check=True)
        elif os.name == "nt":
            # For Windows, use 'start' to open the file with the associated application
            os.system(f"start '{CONFIG_PATH}'")
    except Exception as e:
        rich.print(f":boom: Error opening the configuration file: {e}")


@app.command()
def run(
    local_directory: str = typer.Option(
        "./",
        "--local-directory",
        "-i",
        help="Path to the local directory where images are stored",
    ),
    max_compress_workers: int = typer.Option(
        3,
        "--compress-max",
        help="max workers to compress",
    ),
    max_upload_workers: int = typer.Option(
        3,
        "--upload-max",
        help="max workers to upload",
    ),
):
    """main function"""
    ensure_config_exists()
    config = load_config()
    application_key_id = config["backblaze"]["application_key_id"]
    application_key = config["backblaze"]["application_key"]
    bucket_name = config["backblaze"]["bucket_name"]
    compressor_path = config["local"]["compressor"]

    try:
        # Initialize Backblaze client
        info = InMemoryAccountInfo()
        b2_api = B2Api(info)
        b2_api.authorize_account("production", application_key_id, application_key)
        bucket = b2_api.get_bucket_by_name(bucket_name)
    except InvalidAuthToken as e:
        rich.print(f":no_entry: Failed to authenticate with Backblaze B2: {e}")
        rich.print(
            ":bulb: Please check your [red]application key ID[/red] and [red]application key[/red]."
        )
        sys.exit(0)

    uploaded_files = get_files(bucket)
    local_files = set(os.listdir(local_directory))
    new_images = local_files - uploaded_files

    new_compressed_files = compress_files(
        new_images, local_directory, compressor_path, max_compress_workers
    )
    upload_files(bucket, new_compressed_files, max_upload_workers)
