"""
Storage-related exceptions.
"""

from app.exceptions.base import ApplicationError


class StorageError(ApplicationError):
    """Raised when storage operations fail."""