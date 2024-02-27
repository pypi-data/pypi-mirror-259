from .settings import LoggerSettings

class LoggerConfig:
    @staticmethod
    def generate_config(settings: LoggerSettings):
        config = {
            'version': 1,
            'formatters': {
                'default': {
                    '()': 'MeowthLogger.sources.Formatters.Default'
                },
                'colorised': {
                    '()': 'MeowthLogger.sources.Formatters.Colorised'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': settings.logger_level,
                    'formatter': 'colorised',
                    'stream': 'ext://sys.stdout'
                },
                'file': {
                    'class': 'MeowthLogger.sources.Handlers.CustomHandler',
                    'level': settings.logger_level,
                    'formatter': 'default',
                    'filename': settings.filename,
                    'when': 'midnight',
                    'encoding': settings.encoding,
                    'path': settings.path
                }
            },
            'loggers': {
                'console': {
                    'level': settings.logger_level,
                    'handlers': ['console'],
                    'propagate': False
                },
                'file': {
                    'level': settings.logger_level,
                    'handlers': ['file'],
                    'propagate': False
                },
            },
            'root': {
                'level': settings.logger_level,
                'handlers': ['console', 'file']
            }
        }

        # for using logger for uvicorn
        if settings.use_uvicorn:
            config["loggers"].update({
                "uvicorn.access": {
                    'level': settings.logger_level,
                    'handlers': ['file', 'console'],
                    'propagate': False
                },
                "uvicorn.error": {
                    'level': settings.logger_level,
                    'handlers': ['file', 'console'],
                    'propagate': False
                }
            })

        return config