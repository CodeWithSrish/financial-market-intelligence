"""
Validation-related exceptions.
"""

from app.exceptions.base import ApplicationError


class DataValidationError(ApplicationError):
    """Raised when data validation fails."""