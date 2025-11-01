class HabitatCapacityException(Exception):
    """Raised when a habitat reaches its species capacity."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
