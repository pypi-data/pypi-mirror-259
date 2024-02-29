import logging


def configure_root_logger(stream_handler_level: int = logging.INFO):
    """Configure the root logger to use a custom formatter and a stream handler.

    Notes
    -----
    Only used in the tutorial.
    """
    root = logging.getLogger()
    if not root.handlers:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(stream_handler_level)
        stream_handler.setFormatter(CustomFormatter())
        root.addHandler(stream_handler)


class CustomFormatter(logging.Formatter):
    """
    A custom logging formatter that allows customizable formatting and color-coded output.

    Parameters
    ----------
    fmt : str, optional
        The log message format. Defaults to '%(asctime)s :: %(levelname)-8s :: %(message)s'.
    datefmt : str, optional
        The date format for log timestamps. Defaults to '%H:%M:%S'.

    Attributes
    ----------
    grey : str
        ANSI escape code for grey text.
    yellow : str
        ANSI escape code for yellow text.
    red : str
        ANSI escape code for red text.
    bold_red : str
        ANSI escape code for bold red text.
    reset : str
        ANSI escape code to reset text formatting.

    Methods
    -------
    format(record)
        Format the log record according to the specified log level's formatting.

    Usage
    -----
    formatter = CustomFormatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    Note
    ----
    The ANSI escape codes are used to colorize the output text in supported terminals.
    """

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(
        self,
        fmt=None,
        datefmt=None,
    ) -> None:
        """
        Initialize the CustomFormatter instance.

        Parameters
        ----------
        fmt : str, optional
            The log message format. Defaults to '%(asctime)s :: %(levelname)-8s :: %(message)s'.
        datefmt : str, optional
            The date format for log timestamps. Defaults to '%H:%M:%S'.
        """
        if fmt is None:
            fmt = "%(asctime)s :: %(levelname)-8s :: %(message)s"
        if datefmt is None:
            datefmt = "%H:%M:%S"
        self.custom_format = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.custom_format + self.reset,
            logging.INFO: self.grey + self.custom_format + self.reset,
            logging.WARNING: self.yellow + self.custom_format + self.reset,
            logging.ERROR: self.red + self.custom_format + self.reset,
            logging.CRITICAL: self.bold_red + self.custom_format + self.reset,
        }
        super().__init__(fmt, datefmt)

    def format(self, record):
        """Format the log record according to the specified log level's formatting."""
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=self.datefmt)
        return formatter.format(record)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    configure_root_logger()

    # Start logging
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    logger.exception("...")
