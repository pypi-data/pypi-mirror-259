"""
This sub-package  provides functionality for downloading data from the ExoFOP website.

Outline
-------
:class:`exofop.download.SystemDownloader` : class
    A class for downloading data related to individual stellar systems from ExoFOP.
    
:class:`exofop.download.ExoFOPAuthenticator` : class
    A class for handling authentication with and cookie storage for the ExoFOP server.
    
:class:`exofop.download.TagDownloader` : class
    A class for downloading data using ExoFOP tags.

:class:`exofop.download.System` : class
    A class representing an ExoFOP system identifier, e.g. a TIC ID or a TOI ID.

:class:`exofop.download.TIC` : class
    A class representing a TIC ID.

:class:`exofop.download.TOI` : class
    A class representing a TOI ID.

:class:`exofop.download.OverviewTableAccessor` : class
    A class for providing tables from ExoFOP for a given target.

Example
-------
The following is a basic example of how to use the class :class:`exofop.download.SystemDownloader`
to download data from ExoFOP:

>>> from exofop.download import System, SystemDownloader
>>> system = System("TIC 123456789")
>>> system_loader = SystemDownloader(
...     system=system,
...     data_dir="path/to/directory/to/store/downloaded/tags",
... )
>>> tags = system_loader.time_series.tags
>>> system_loader.download(tags[:5])

For a more detailed introduction, consult the tutorial :doc:`notebooks/1_download_from_ExoFOP`.

Classes
-------
"""

from .authenticator import ExoFOPAuthenticator
from .identifiers import System, TIC, TOI
from .downloaders import TagDownloader, SystemDownloader, OverviewTableAccessor

__all__ = [
    "ExoFOPAuthenticator",
    "System",
    "TIC",
    "TOI",
    "TagDownloader",
    "SystemDownloader",
    "OverviewTableAccessor",
]
