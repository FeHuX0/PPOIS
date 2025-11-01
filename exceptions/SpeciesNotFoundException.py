class SpeciesNotFoundException(Exception):
    """Raised when a species record is missing."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
