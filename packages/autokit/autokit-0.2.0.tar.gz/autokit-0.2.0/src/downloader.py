import os

import requests
import zipfile
import tempfile
from pathlib import Path


def download(tool_directory: Path, url: str, chunk_size=1024, progress_callback=None) -> None:
    """
    Downloads a zip file from the given URL and extracts it.
    """
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    bytes_downloaded = 0

    with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as fp:
        temp_file_name = fp.name
        for chunk in response.iter_content(chunk_size=chunk_size):
            bytes_downloaded += len(chunk)
            fp.write(chunk)
            if progress_callback:
                progress_callback(bytes_downloaded / total_size_in_bytes * 100)

    with zipfile.ZipFile(temp_file_name, 'r') as zip_ref:
        zip_ref.extractall(tool_directory)

    os.remove(temp_file_name)
