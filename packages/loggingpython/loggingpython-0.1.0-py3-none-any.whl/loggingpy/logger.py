from .log_levels import LogLevel


class Logger:
    """
    Simple logger class for custom logging functionality.
    """

    _SUPPORTED_LEVELS = list(LogLevel)

    def __init__(self, name: str = "Root-Logger",
                 min_loglevel: LogLevel = LogLevel.INFO,
                 max_loglevel: LogLevel = LogLevel.CRITICAL) -> None:

        self.name = name
        self.min_loglevel = min_loglevel
        self.max_loglevel = max_loglevel

    def _validate_loglevel(self, loglevel: LogLevel) -> None:
        """
        Validates the provided log level.

        Args:
            level (LogLevel): The log level to be validated.

        Raises:
            ValueError: If the loglevel is not supported.
        """

        if loglevel not in self._SUPPORTED_LEVELS:
            raise ValueError

    def _loglevel_over_min_loglevel(self, loglevel: LogLevel) -> bool:
        return self._SUPPORTED_LEVELS.index(loglevel) >= \
            self._SUPPORTED_LEVELS.index(self.min_loglevel)

    def _loglevel_under_max_loglevel(self, loglevel: LogLevel) -> bool:
        return self._SUPPORTED_LEVELS.index(loglevel) <= \
            self._SUPPORTED_LEVELS.index(self.min_loglevel)

    def _log(self, message: str, loglevel: LogLevel = LogLevel.INFO) -> None:
        """
        Logs a message with the specified log level and includes
            a full traceback.

        Args:
            message (str): The message to log.
            loglevel (LogLevel, optional): The log level. Defaults to ERROR.
                Must be one of the supported levels:
                DEBUG, INFO, WARNING, ERROR, CRITICAL.

        Raises:
            ValueError: If the level is not supported.
        """

        try:
            self._validate_loglevel(loglevel)
            if self._loglevel_over_min_loglevel(loglevel):
                if self._loglevel_under_max_loglevel(loglevel):
                    print(f"[{self.name}]: [{loglevel.name}]: {message}")
        except ValueError as e:
            self.error(f"ValueError: {e}")

    def debug(self, message: str) -> None:
        """
        Logs a message at the DEBUG level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """

        self.log(message, loglevel=LogLevel.DEBUG)

    def info(self, message: str) -> None:
        """
        Logs a message at the INFO level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """

        self._log(message, loglevel=LogLevel.INFO)

    def warning(self, message: str) -> None:
        """
        Logs a message at the WARNING level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """

        self._log(message, loglevel=LogLevel.WARNING)

    def error(self, message: str) -> None:
        """
        Logs a message at the ERROR level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """

        self._log(message, loglevel=LogLevel.ERROR)

    def critical(self, message: str) -> None:
        """
        Logs a message at the CRITICAL level.

        Args:
            message (str): The message to log.

        Raises:
            ValueError: If the level is not supported.
        """
        self._log(message, loglevel=LogLevel.CRITICAL)
