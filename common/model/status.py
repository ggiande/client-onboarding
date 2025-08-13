"""Enum"""
from enum import Enum

class Status(Enum):
    """A product may be classified and saved, arrived and pending to 
    be classified, marked as a duplicate, failed to be processed, and
    in the midst of processing.

    Args:
        Enum (_type_): state of product
    """
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"
    ARRIVED = "ARRIVED"
    DUPLICATE = "DUPLICATE"
