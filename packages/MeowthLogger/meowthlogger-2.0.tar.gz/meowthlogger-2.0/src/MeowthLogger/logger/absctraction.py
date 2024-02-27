from abc import ABC

class AbstractLogger(ABC):
    """Abstract class for composition logger in to custom class
    """

    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def critical(self, message):
        self.logger.critical(message)