# Patch Loader and Server

## Overview

This repository contains two scripts designed to manage and serve software patches efficiently:

1. **`loader.py`**: Implements the logic for downloading all patches starting from a specified version (`curr_patch_version`) up to the latest available version.
2. **`server.py`**: A simple HTTP server that serves the downloaded patches to clients.

## Setup

### Creating a Virtual Environment
To ensure a clean Python environment for this project, it is recommended to create a virtual environment:

1. Create the virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
    - On Windows:
    ```bash
    .\.venv\Scripts\activate
    ```
    - On macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install flask asyncio aiohttp aiofiles
    ```

## Usage

### `loader.py`
- Functionality: Downloads patches sequentially from the given `curr_patch_version` to the latest version.
- Configuration: Update the `curr_patch_version` parameter to the desired starting version.
- Execution: Run the script to automatically fetch all missing patches.

### `server.py`
- Functionality: Serves the patches via an HTTP server for client requests.
- Setup: Place the downloaded patches in the appropriate directory for the server to access.
- Execution: Start the server to allow clients to fetch the required patches.

## Requirements
- Python 3.x

## GNU GENERAL PUBLIC LICENSE
### Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc.  
51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA  
Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

### Preamble

The GNU General Public License is a free, copyleft license for software and other kinds of works. The licenses for most software are designed to take away your freedom to share and change it. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program— to make sure it remains free software for all its users.


### Full License Text
[Full License Text](https://www.gnu.org/licenses/gpl-3.0.html)