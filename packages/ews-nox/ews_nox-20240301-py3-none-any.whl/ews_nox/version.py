"""
# Purpose

Provide access to version information as well as dependencies

# Usage example


```python
import ews_nox

print(ews_nox.version_info())
```

# Tests

"""

from __future__ import annotations

import platform
import sys
from importlib import import_module  # noqa: F401
from pathlib import Path

__all__ = ("VERSION", "version_info")

from importlib import metadata

VERSION = metadata.version("ews_nox")


def version_info() -> str:
    """
    Show the version info

    Example:
        ```python
        import ews_nox

        print(ews_nox.version_info())
        ```

    """

    optional_deps = []

    info = {
        "ews_nox version": VERSION,
        "install path": Path(__file__).resolve().parent,
        "python version": sys.version,
        "platform": platform.platform(),
        "optional deps. installed": optional_deps,
    }
    return "\n".join(
        "{:>30} {}".format(k + ":", str(v).replace("\n", " ")) for k, v in info.items()
    )
