from __future__ import annotations

from typing import Any

from diskcache_fernet.cache import FernetCache
from diskcache_fernet.disk import FernetDisk
from diskcache_fernet.fanout import FernetFanoutCache
from diskcache_fernet.secret import SecretValue

__all__ = ["FernetCache", "FernetFanoutCache", "SecretValue", "FernetDisk"]

__version__: str


def __getattr__(name: str) -> Any:  # pragma: no cover
    from importlib.metadata import version

    if name == "__version__":
        return version("diskcache-fernet")

    error_msg = f"The attribute named {name!r} is undefined."
    raise AttributeError(error_msg)
