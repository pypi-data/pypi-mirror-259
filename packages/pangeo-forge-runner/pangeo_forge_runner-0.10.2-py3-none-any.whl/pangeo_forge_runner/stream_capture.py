import contextlib
import logging
import sys


class LoggingStream:
    """
    File-like object that redirects to a python logger.

    Minimal implementation used only to replace sys.stdout, stderr.
    """

    def __init__(self, log: logging.Logger, level: str, extra: dict):
        self.log = log
        self.level = level
        self.extra = extra

    def write(self, message):
        self.log.log(self.level, message, extra=self.extra)


@contextlib.contextmanager
def redirect_stdout(log: logging.Logger, extra: dict):
    logging_stdout = LoggingStream(log, logging.INFO, extra)
    original_stdout = sys.stdout
    sys.stdout = logging_stdout
    try:
        yield
    finally:
        sys.stdout = original_stdout


@contextlib.contextmanager
def redirect_stderr(log: logging.Logger, extra: dict):
    logging_stderr = LoggingStream(log, logging.INFO, extra)
    original_stderr = sys.stdout
    sys.stderr = logging_stderr
    try:
        yield
    finally:
        sys.stderr = original_stderr
