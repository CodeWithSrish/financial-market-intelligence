"""
Warehouse-related exceptions.
"""

from app.exceptions.base import ApplicationError


class WarehouseError(ApplicationError):
    """Raised when warehouse operations fail."""