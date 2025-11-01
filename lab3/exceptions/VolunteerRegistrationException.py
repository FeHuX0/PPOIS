class VolunteerRegistrationException(Exception):
    """Raised when volunteer registration fails."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
