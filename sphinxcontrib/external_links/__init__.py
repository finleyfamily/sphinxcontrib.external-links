"""Sphinx extension sphinxcontrib.external-links."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # cov: ignore
    # package is not installed
    __version__ = "0.0.0"
