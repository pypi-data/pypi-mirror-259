import logging
import logging.config

from .absctraction import AbstractLogger
from .settings import LoggerSettings

from ..constants import (
    DEFAULT_LOGGING_FILENAME,
    DEFAULT_LOGGING_LEVEL,
    DEFAULT_ENCODING,
    DEFAULT_PATH
)
from .config import LoggerConfig
from .log_parser import LogParser

class Logger(AbstractLogger, LogParser):
    settings: LoggerSettings

    def __init__(
            self,
            logger_level: str = DEFAULT_LOGGING_LEVEL,
            filename: str = DEFAULT_LOGGING_FILENAME,
            encoding: str = DEFAULT_ENCODING,
            path: str = DEFAULT_PATH,
            use_uvicorn: bool = False
        ):

        self.settings = LoggerSettings(
            logger_level=logger_level,
            filename=filename,
            encoding=encoding,
            path=path,
            use_uvicorn=use_uvicorn,
        )

        logging.config.dictConfig(
            self.config
        )

        self.logger = logging.getLogger()

    @property
    def config(self):
        return LoggerConfig.generate_config(self.settings)