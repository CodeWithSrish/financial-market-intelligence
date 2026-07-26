"""
Custom exceptions for the Financial Market Intelligence Platform.
"""

from app.exceptions.api import (
    APIAuthenticationError,
    APIConnectionError,
    APIRateLimitError,
    APITimeoutError,
)
from app.exceptions.base import ApplicationError
from app.exceptions.storage import StorageError
from app.exceptions.validation import DataValidationError
from app.exceptions.warehouse import WarehouseError

__all__ = [
    "ApplicationError",
    "APIConnectionError",
    "APITimeoutError",
    "APIRateLimitError",
    "APIAuthenticationError",
    "DataValidationError",
    "StorageError",
    "WarehouseError",
]