"""Compress and convert image to wedp format and upload them to B2 concurrencely"""

import subprocess
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from b2sdk.bucket import Bucket
import typer

__version__ = "0.1.1"
app = typer.Typer()


def get_files(bucket: Bucket):
    """retrieve file list from B2"""
    uploaded_files = set(file_version.file_name for file_version, _ in bucket.ls())
    return uploaded_files


def compress(input_path, output_path, compressor_path: str):
    """compress and convert to webp"""
    try:
        subprocess.run([compressor_path, input_path, "-o", output_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess failed with return code {e.returncode}")


def compress_files(
    new_images: set,
    local_directory: str,
    compressor_path: str,
    max_workers: int,
):
    """batch compress images"""
    compressed_images = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for f in new_images:
            if f.endswith((".jpg", ".jpeg", ".png")):
                input_path = os.path.join(local_directory, f)
                output_path = os.path.join(
                    local_directory, os.path.splitext(f)[0] + ".webp"
                )
                futures.append(
                    executor.submit(compress, input_path, output_path, compressor_path)
                )
                compressed_images.append(output_path)

        for future in futures:
            future.result()
    return compressed_images


def upload(bucket: Bucket, local_file_path: str, b2_file_name: str):
    """upload single file"""
    bucket.upload_local_file(local_file=local_file_path, file_name=b2_file_name)
    return f"Uploaded {local_file_path} to {b2_file_name}"


def upload_files(bucket: Bucket, new_compressed_files: list, max_workers: int):
    """upload files in concurrency"""
    # Use ThreadPoolExecutor to upload files in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {
            executor.submit(upload, bucket, file, os.path.basename(file)): file
            for file in new_compressed_files
        }

        for future in as_completed(future_to_file):
            file = future_to_file[future]
            try:
                result = future.result()
                print(result)
            except Exception as exc:
                print(f"{file} generated an exception: {exc}")
