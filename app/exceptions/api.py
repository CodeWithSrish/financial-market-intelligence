"""
API-related exceptions.
"""

from app.exceptions.base import ApplicationError


class APIError(ApplicationError):
    """Base class for API exceptions."""


class APIConnectionError(APIError):
    """Raised when an API connection fails."""


class APITimeoutError(APIError):
    """Raised when an API request times out."""


class APIRateLimitError(APIError):
    """Raised when an API rate limit is exceeded."""


class APIAuthenticationError(APIError):
    """Raised when API authentication fails."""