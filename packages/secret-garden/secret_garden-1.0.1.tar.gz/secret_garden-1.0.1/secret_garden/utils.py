"""Utility objects and functions for secret_garden package."""

# Built-in imports
from os import PathLike
from pathlib import Path


# CONSTANTS
ALLOWED_FORMATS = [
    "env",
    "environ",
    "json",
    "toml",
    "yaml",
]

FILE_ENCODING = "utf-8"


def read_file(path: Path | PathLike | str) -> str:
    """Read a file and return its contents"""

    with open(path, "r", encoding=FILE_ENCODING) as file_:
        return file_.read()
