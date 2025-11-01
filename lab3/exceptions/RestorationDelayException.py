class RestorationDelayException(Exception):
    """Raised when restoration timelines slip."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
