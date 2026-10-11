"""Root pytest configuration and hooks."""

import sys
from pathlib import Path
from typing import Any


def pytest_collect_file(file_path: Path, parent: Any) -> None:
    """Clear cached test_utils between exercise modules during collection."""
    sys.modules.pop("test_utils", None)


def pytest_pycollect_makemodule(module_path: Path, parent: Any) -> None:
    """Clear cached test_utils before importing each test module."""
    sys.modules.pop("test_utils", None)
