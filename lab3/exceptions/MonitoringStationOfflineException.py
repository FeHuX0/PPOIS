class MonitoringStationOfflineException(Exception):
    """Raised when a monitoring station is inactive."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
