from __future__ import annotations

import shutil
from pathlib import Path


def rm_file(my_file: Path) -> None:
    """
    Remove the specified file if it exists.

    Args:
        my_file (Path): Path to the file to be removed.

    Raises:
        OSError: If there is an error during the removal process.
    """
    if my_file.is_file():
        try:
            my_file.unlink()
        except OSError as e:
            msg = f"Error removing file: {e}"
            raise OSError(msg) from None


def rm_dir(my_dir: Path) -> None:
    """
    Remove the specified directory if it exists.

    Args:
        my_dir (Path): Path to the directory to be removed.

    Raises:
        OSError: If there is an error during the removal process.
    """
    if my_dir.is_dir():
        try:
            shutil.rmtree(my_dir)
        except OSError as e:
            msg = f"Error removing directory: {e}"
            raise OSError(msg) from None
