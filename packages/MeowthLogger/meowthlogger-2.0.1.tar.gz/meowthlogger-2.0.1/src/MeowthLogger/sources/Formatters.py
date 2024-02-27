import logging
import time
import os

from colorama import Style, Fore, Back
from ..constants import DEFAULT_FORMATTER

class Default(logging.Formatter):
    def __init__(self):
        logging.Formatter.__init__(self, "")

    def format(self, record):

        format_orig = self._fmt

        message = record.getMessage()
        created = self.converter(record.created)
        created = time.strftime(self.default_time_format, created)

        self._fmt = format_orig

        if record.levelno == logging.INFO:
            levelname = "INFO"

        elif record.levelno == logging.ERROR:
            levelname = "ERROR"

        elif record.levelno == logging.WARN:
            levelname = "WARNING"

        elif record.levelno == logging.CRITICAL:
            levelname = "CRITICAL"
        
        elif record.levelno == logging.DEBUG:
            levelname = "DEBUG"

        datetime = "[" + created + "]"

        filename = record.filename
        filename = record.pathname.replace(os.path.abspath(""), ".")

        line = f"{record.lineno}"

        result = f"{datetime} {levelname} in {filename} line {line}: {message}"
        result = DEFAULT_FORMATTER.format(
            datetime=datetime,
            levelname=levelname,
            filename=filename,
            line=line,
            message=message
        )

        return result
    
    


class Colorised(logging.Formatter):

    def __init__(self):
        logging.Formatter.__init__(self, "")


    def format(self, record):

        format_orig = self._fmt

        message = record.getMessage()
        created = self.converter(record.created)
        created = time.strftime(self.default_time_format, created)

        self._fmt = format_orig

        if record.levelno == logging.INFO:
            levelname = Fore.GREEN + "INFO" + Fore.RESET

        elif record.levelno == logging.ERROR:
            levelname = Fore.RED + "ERROR" + Fore.RESET

        elif record.levelno == logging.WARN:
            levelname = Fore.YELLOW + "WARNING" + Fore.RESET

        elif record.levelno == logging.CRITICAL:
            levelname = Back.RED + " CRITICAL " + Back.RESET
        
        elif record.levelno == logging.DEBUG:
            levelname = Fore.LIGHTBLACK_EX + "DEBUG" + Fore.RESET

        datetime = "[" + Style.DIM + created + Style.NORMAL + "]"

        filename = Fore.LIGHTYELLOW_EX + record.filename + Fore.RESET
        filename = Fore.LIGHTYELLOW_EX + record.pathname.replace(os.path.abspath(""), ".") + Fore.RESET

        line = Fore.LIGHTYELLOW_EX + f"{record.lineno}" + Fore.RESET

        result = DEFAULT_FORMATTER.format(
            datetime=datetime,
            levelname=levelname,
            filename=filename,
            line=line,
            message=message
        )

        return result
