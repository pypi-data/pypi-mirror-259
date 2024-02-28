# weblaze

<p align="center">
<img src="https://github.com/cybershang/weblaze/blob/93de39f2c842a900a7b31046724b30459f59314e/docs/media/weblaze.gif" width="360"/>
</p>

<p align="center">
<a href="https://pypi.org/project/weblaze/"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/weblaze"></a>
<a href="https://pypistats.org/packages/weblaze"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/weblaze"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
</p>


**Usage**:

```console
$ weblaze [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `edit`: Edit the configuration file in the...

- `init`: Initialize and generate a configuration...

- `run`: main function

## Configuration

  ```yaml
  backblaze:
      application_key_id: ***
      application_key: ***
      bucket_name: ***
  local:
      compressor: ***\cwebp.exe
  ```

## Commands



### `edit`

Edit the configuration file in the system's default editor.

**Usage**:

```console
$ edit [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

### `init`

Initialize and generate a configuration file in the user's .config directory.

**Usage**:

```console
$ init [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

### `run`

main function

**Usage**:

```console
$ run [OPTIONS]
```

**Options**:

- `-i, --local-directory TEXT`: Path to the local directory where images are stored [default: ./]
- `--compress-max INTEGER`: max workers to compress [default: 3]
- `--upload-max INTEGER`: max workers to upload [default: 3]
- `--help`: Show this message and exit.

```mermaid
flowchart TD
    w(weblaze) --> 1.jpg --> cwebp1(cwebp 1)
    w --> 2.jpg --> cwebp2(cwebp 2)
    w --> 3.jpg --> cwebp3(cwebp 3)
    cwebp1 --> |compress| 1.webp
    cwebp2 --> |compress| 2.webp
    cwebp3 --> |compress| 3.webp
    1.webp --> |upload| b1[B2_uploader_1] --> B2(Backblaze)
    2.webp --> |upload| b2[B2_uploader_2] --> B2
    3.webp --> |upload| b3[B2_uploader_3] --> B2
```
