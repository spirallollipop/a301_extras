from pathlib import Path

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("plot_utils")
except PackageNotFoundError:
    __version__ = "unknown version"

try:
    from ._version import version_tuple
except ImportError:
    version_tuple = (0, 0, "unknown version")

print("in a301_extras init")
