class SampleContaminationException(Exception):
    """Raised when a sample integrity is compromised."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
