import os
import re
import shutil
from enum import Enum
from pathlib import Path
from typing import List, Literal, Optional

import semantic_version
from download import download as fetch

VERSION_REGEX = re.compile(r"(\d+\.\d+(?:\.\d+)?)", flags=re.MULTILINE)


# String enumerator.
class StrEnum(str, Enum):
    def __str__(self) -> str:
        return str(self.value)


# Python hack in order to allow static properties.
class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


# Resolves input path and its environment variables
# indistinctly from the current OS.
def path(path: str) -> str:
    return str(Path(os.path.expandvars(path)).resolve())


# Splits input string returning the left-most word
# and the rest of the string.
def next_arg(string: str) -> str:
    lpos = string.find(" ")
    return (string[:lpos], string[lpos + 1 :]) if lpos != -1 else (string, "")


# Creates a file or a directory in the specified path (overwritting).
def create(path: str, data: List[str] = [""], dir: bool = False) -> None:
    if dir:
        os.makedirs(str(path), exist_ok=True)
    else:
        dirs = os.path.dirname(str(path))
        if dirs:
            os.makedirs(dirs, exist_ok=True)
        data = [str(line) + "\n" for line in data]
        with open(str(path), "w") as f:
            f.writelines(data)


# Reads a file in the specified path.
def read(path: str) -> List[str]:
    with open(str(path), "r") as f:
        return f.read().splitlines()


# Checks if the specified path exists and whether it is a file or a directory.
def exists(path: str) -> Optional[Literal["file", "dir"]]:
    if not os.path.exists(str(path)):
        return None
    elif os.path.isdir(str(path)):
        return "dir"
    elif os.path.isfile(str(path)):
        return "file"
    else:
        return None


# Moves a file or a directory to the specified path.
def move(source_path: str, dest_path: str) -> None:
    shutil.move(str(source_path), str(dest_path))


# Removes a file or a directory in the specified path.
def remove(path: str, dir: bool = False) -> None:
    if dir:
        shutil.rmtree(str(path))
    else:
        os.remove(str(path))


# Extracts a zip, tar, gztar, bztar, or xztar file in the specified path.
def extract(source_path: str, dest_path: str) -> None:
    shutil.unpack_archive(str(source_path), str(dest_path))


# Downloads a file to the specified path.
def download(url: str, path: str) -> None:
    fetch(str(url), str(path), progressbar=False, replace=True, verbose=False)


# Checks whether an input has a compatible version with target.
def has_compatible_version(input: str, target: str) -> bool:
    if not target:
        return False

    try:
        target = semantic_version.SimpleSpec(target)
    except Exception:
        return False

    for version in VERSION_REGEX.findall(input):
        if not version:
            continue

        # Add base minor if not present
        if len(version.split(".")) < 3:
            version += ".0"

        try:
            version = semantic_version.Version(version)
        except Exception:
            continue

        if version in target:
            return True

    return False
