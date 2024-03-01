__all__ = ("VERSION", "version_info")


import sys

from packaging.version import Version

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata  # pragma: no cover


VERSION = metadata.version("ews_core_config")
Version(VERSION)._version  # We make sure we generate a valid version!


def version_info() -> str:
    """
    Show the version info

    Example:
        ```python
        import ews_core_config

        print(ews_core_config.version_info())
        ```

    """
    import platform
    import sys
    from importlib import import_module  # noqa: F401
    from pathlib import Path

    optional_deps = []

    info = {
        "ews_core_config version": VERSION,
        "install path": Path(__file__).resolve().parent,
        "python version": sys.version,
        "platform": platform.platform(),
        "optional deps. installed": optional_deps,
    }
    return "\n".join("{:>30} {}".format(k + ":", str(v).replace("\n", " ")) for k, v in info.items())
