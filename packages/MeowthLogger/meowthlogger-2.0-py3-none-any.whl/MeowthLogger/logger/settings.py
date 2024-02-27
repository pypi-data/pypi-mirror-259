class LoggerSettings:
    def __init__(
        self,
        logger_level: str,
        filename: str,
        encoding: str,
        path: str,
        use_uvicorn: bool,
    ):
        self.logger_level = logger_level
        self.filename = filename
        self.encoding = encoding
        self.path = path
        self.use_uvicorn = use_uvicorn