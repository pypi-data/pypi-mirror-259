import inspect
import os
import re
from pathlib import Path
from typing import (
    Union,
)

from bs4 import BeautifulSoup

html_regex = r"<!.*?->|^--html"

project_root = os.getcwd()


def load_html_to_soup(path: Union[str, Path], parser: str = "html.parser"):
    """
    Load an HTML file from a specified path and return a BeautifulSoup object.
    The function automatically determines the base path using the caller's file path.

    :param path: The path to the HTML file.
    :return: A BeautifulSoup object of the loaded HTML file.
    """

    # If the path is multiple lines or starts with --html, it contains the HTML
    if isinstance(path, str) and ("\n" in path or path.startswith("--html")):
        file_contents = re.sub(html_regex, "", path, flags=re.DOTALL)

        first_line = file_contents.split("\n")[0]

        if "<?xml" in first_line:
            parser = "xml"

        return BeautifulSoup(file_contents, parser)

    if "~/" in str(path) or bool(re.match(r"^[a-zA-Z]", str(path))):
        path = Path(str(path).replace("~/", ""))

        base_path = project_root
    else:
        # Convert the path to a `Path` object if necessary
        if not isinstance(path, Path):
            path = Path(path)

        # Traverse the stack to find the first frame outside of the 'weba' package
        for frame_info in inspect.stack():
            frame_file = Path(frame_info.filename)
            if "weba" not in frame_file.parts:
                # Use the caller's file path to determine the base path
                base_path = frame_file.parent
                break
            else:
                base_path = None
        else:
            # If no caller is found outside of 'weba', default to the current working directory
            base_path = Path.cwd()

    # Resolve the path relative to the base path
    resolved_path = base_path / path

    # Ensure the file exists
    if not resolved_path.exists():
        raise FileNotFoundError(f"The file at {resolved_path} does not exist.")

    # Read the file and parse it with BeautifulSoup
    with open(resolved_path, "r", encoding="utf-8") as file:
        file_contents = file.read()
        # Remove comments
        file_contents = re.sub(html_regex, "", file_contents, flags=re.DOTALL)

        first_line = file_contents.split("\n")[0]

        if "<?xml" in first_line:
            parser = "xml"

        return BeautifulSoup(file_contents, parser)
