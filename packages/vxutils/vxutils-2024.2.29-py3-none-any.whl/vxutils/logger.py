"""logging module patching"""

from __future__ import absolute_import


import logging
import collections
from logging import LogRecord
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Dict, Union, Any, Optional, List, Callable
from vxutils import __vxutils__

try:
    import colorama
except ImportError:
    pass
else:
    colorama.init()

__all__ = (
    "init_colored_console",
    "init_logfile",
    "init_logging",
    "set_quanttime_func",
    "debug",
    "info",
    "warning",
    "error",
    "critical",
    "setLevel",
    "VXColoredFormatter",
    "VXLogRecord",
)

__log_files__: List[Path] = []
__logger_root__: str = __vxutils__


# Returns escape codes from format codes
def esc(*x: str) -> str:
    """escape codes from format codes"""
    return "\033[" + ";".join(x) + "m"


# The initial list of escape codes
escape_codes = {
    "reset": esc("0"),
    "bold": esc("01"),
}

# The color names
COLORS = ["black", "red", "green", "yellow", "blue", "purple", "cyan", "white"]

PREFIXES = [
    # Foreground without prefix
    ("3", ""),
    ("01;3", "bold_"),
    # Foreground with fg_ prefix
    ("3", "fg_"),
    ("01;3", "fg_bold_"),
    # Background with bg_ prefix - bold/light works differently
    ("4", "bg_"),
    ("10", "bg_bold_"),
]

for prefix, prefix_name in PREFIXES:
    for code, name in enumerate(COLORS):
        escape_codes[prefix_name + name] = esc(prefix + str(code))


def parse_colors(sequence: str) -> str:
    """Return escape codes from a color sequence."""
    return "".join(escape_codes[n] for n in sequence.split(",") if n)


# The default colors to use for the debug levels
default_log_colors = {
    "DEBUG": "bold_green",
    "INFO": "white",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "bold_red",
}

# The default format to use for each style
default_formats = {
    "%": "%(log_color)s%(levelname)s:%(name)s:%(message)s",
    "{": "{log_color}{levelname}:{name}:{message}",
    "$": "${log_color}${levelname}:${name}:${message}",
}


class VXLogRecord:
    """
    A wrapper class around the LogRecord class.

    1. 增加颜色字段: %(log_color)s
    2. 增加自定义事件字段 %(quanttime)s --用于自定义日志时间

    """

    class __dict(collections.defaultdict):
        def __missing__(self, key: str) -> Any:
            try:
                return parse_colors(key)
            except Exception as err:
                raise KeyError(
                    f"{key} is not a valid record attribute or color sequence"
                ) from err

    def __init__(self, record: logging.LogRecord) -> None:
        self.__dict__ = self.__dict()
        self.__dict__.update(record.__dict__)
        self.__record = record

    def __getattr__(self, name: str) -> Any:
        return getattr(self.__record, name)


class VXFormatter(logging.Formatter):
    __quanttime_func__: Callable[..., datetime] = datetime.now

    @classmethod
    def set_quanttime_func(cls, func: Callable[..., datetime]) -> None:
        cls.__quanttime_func__ = func

    def format(self, record: LogRecord) -> str:
        record.quanttime = self.__quanttime_func__().strftime(
            self.datefmt or "%Y-%m-%d %H:%M:%S.%f"
        )
        return super().format(record)


class VXColoredFormatter(VXFormatter):
    """
    A formatter that allows colors to be placed in the format string.

    Intended to help in creating more readable logging output.
    """

    def __init__(
        self,
        fmt: str = "",
        datefmt: str = "",
        style: str = "%",
        log_colors: Optional[Dict[str, str]] = None,
        reset: bool = True,
        secondary_log_colors: Optional[Dict[str, str]] = None,
    ) -> None:
        """
        Set the format and colors the ColoredFormatter will use.

        The ``fmt``, ``datefmt`` and ``style`` args are passed on to the
        ``logging.Formatter`` constructor.

        The ``secondary_log_colors`` argument can be used to create additional
        ``log_color`` attributes. Each key in the dictionary will set
        ``{key}_log_color``, using the value to select from a different
        ``log_colors`` set.

        :Parameters:
        - fmt (str): The format string to use
        - datefmt (str): A format string for the date
        - log_colors (dict):
            A mapping of log level names to color names
        - reset (bool):
            Implictly append a color reset to all records unless False
        - style ('%' or '{' or '$'):
            The format style to use. (*No meaning prior to Python 3.2.*)
        - secondary_log_colors (dict):
            Map secondary ``log_color`` attributes. (*New in version 2.6.*)
        """
        if fmt is None:
            if sys.version_info > (3, 2):
                fmt = default_formats[style]
            else:
                fmt = default_formats["%"]

        super().__init__(fmt, datefmt, style)
        self.log_colors = log_colors if log_colors is not None else default_log_colors
        self.secondary_log_colors = secondary_log_colors
        self.reset = reset

    def color(self, log_colors: Dict[str, str], name: str) -> str:
        """Return escape codes from a ``log_colors`` dict."""
        return parse_colors(log_colors.get(name, ""))

    def format(self, record: logging.LogRecord) -> str:
        """Format a message from a record object."""
        record = VXLogRecord(record)
        record.log_color = self.color(self.log_colors, record.levelname)
        record.quanttime = self.__quanttime_func__().strftime(
            self.datefmt or "%Y-%m-%d %H:%M:%S.%f"
        )

        # Set secondary log colors
        if self.secondary_log_colors:
            for name, log_colors in self.secondary_log_colors.items():
                color = self.color(log_colors, record.levelname)
                setattr(record, f"{name}_log_color", color)

        # Format the message
        if sys.version_info > (2, 7):
            message = super().format(record)
        else:
            message = logging.Formatter.format(self, record)

        # Add a reset code to the end of the message
        # (if it wasn't explicitly added in format str)
        if self.reset and not message.endswith(escape_codes["reset"]):
            message += escape_codes["reset"]

        return message


__COLOR_BASIC_FORMAT__ = (
    "%(log_color)s%(quanttime)s [%(process)s:%(threadName)s - %(funcName)s@%(filename)s:%(lineno)d]"
    " %(levelname)s: %(message)s%(reset)s"
)

__BASIC_FORMAT__ = (
    "%(quanttime)s [%(process)s:%(threadName)s - %(funcName)s@%(filename)s:%(lineno)d]"
    " %(levelname)s: %(message)s"
)


def init_colored_console(
    log_level: Union[str, int] = "INFO",
    *,
    logger: logging.Logger = logging.root,
) -> None:
    """为logging模块打补丁"""
    logger.setLevel(log_level)
    if logger is not logging.root:
        logging.root.handlers = []

    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            handler.setFormatter(VXColoredFormatter(fmt=__COLOR_BASIC_FORMAT__))
            handler.setLevel(log_level)
            break
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(VXColoredFormatter(fmt=__COLOR_BASIC_FORMAT__))
        console_handler.setLevel(log_level)
        logger.addHandler(console_handler)
        logger.warning("console handler added")
    # 添加file handler


def init_logfile(
    log_file: Union[str, Path] = "log/message.log",
    log_level: Union[str, int] = "INFO",
    *,
    logger: logging.Logger = logging.root,
) -> None:
    """为logging模块打补丁"""
    log_file = Path(log_file)
    global __log_files__
    if log_file in __log_files__:
        return

    log_dir = log_file.parent
    log_dir.mkdir(parents=True, exist_ok=True)
    file_handler = TimedRotatingFileHandler(
        log_file, when="D", interval=1, backupCount=7
    )
    file_handler.setFormatter(VXFormatter(fmt=__BASIC_FORMAT__))
    file_handler.setLevel(log_level)

    logger = logging.root
    # logger = logging.getLogger(__logger_root__)
    logger.addHandler(file_handler)
    __log_files__.append(log_file)
    logger.warning(f"file handler added: {log_file.absolute()}")


def init_logging(
    log_file: Union[str, Path] = "log/message.log",
    log_level: Union[str, int] = "INFO",
    *,
    logger: logging.Logger = logging.root,
) -> None:
    init_colored_console(log_level, logger=logger)
    init_logfile(log_file, log_level, logger=logger)


_logger = logging.getLogger(__logger_root__)
init_colored_console(log_level="INFO", logger=_logger)

root = _logger
debug = _logger.debug
info = _logger.info
warning = _logger.warning
error = _logger.error
critical = _logger.critical
setLevel = _logger.setLevel

set_quanttime_func = VXFormatter.set_quanttime_func


if __name__ == "__main__":
    init_logging(log_level="DEBUG")
    init_logging()
    init_logging()
    init_logging()
    init_logging(log_level="INFO")
    logging.debug("debug")
    logging.info("hello")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
    root.info("info")
