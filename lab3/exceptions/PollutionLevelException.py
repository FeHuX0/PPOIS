class PollutionLevelException(Exception):
    """Raised when pollution thresholds are exceeded."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
