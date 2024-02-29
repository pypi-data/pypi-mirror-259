import os


PACKAGEDIR: str = os.path.abspath(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)),  # exofop/utils
        os.pardir
        )
)

COOKIES_DIR: str = os.path.join(PACKAGEDIR, "cookies")

CONFIG_DIR : str = os.path.join(PACKAGEDIR, "config")

MPLSTYLE: str = f"{PACKAGEDIR}/config/style.mplstyle"
""" Path to stylesheet for matplotlib.

It is useful for users who create their own figures and want their figures following
the package style.

    Examples
    --------
    Create a scatter plot with a custom size using Lightkurve's style.

        >>> with plt.style.context(MPLSTYLE):  # doctest: +SKIP
        >>>     ax = plt.figure(figsize=(6, 3)).gca()  # doctest: +SKIP

"""
