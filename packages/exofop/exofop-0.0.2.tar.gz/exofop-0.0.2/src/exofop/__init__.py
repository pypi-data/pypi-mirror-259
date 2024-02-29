import os
import logging
from exofop.utils.urls import BASE_URL

logger = logging.getLogger("exofop")
logger.setLevel(logging.INFO)

PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))
""" Path to the package directory. """

BASE_URL = BASE_URL
""" Base URL for the ExoFOP website. """

COOKIES_DIR = os.path.join(PACKAGEDIR, "cookies")
""" Directory where the cookies are stored. """

MPLSTYLE = f"{PACKAGEDIR}/config/style.mplstyle"
"""Stylesheet for matplotlib.

It is useful for users who create their own figures and want their figures following
the package' style.

Examples
--------
Create a scatter plot with a custom size using the stylesheet.

>>> with plt.style.context(MPLSTYLE):  # doctest: +SKIP
>>>     ax = plt.figure(figsize=(6, 3)).gca()  # doctest: +SKIP
"""
