"""Enum"""
from enum import Enum

class DataFormat(Enum):
    """Each data source will present data in different formats.
    
    Args:
        Enum (_type_): expected data format
    """
    CSV = "CSV"
    PROTO = "PROTO"
    JSON = "JSON"
    UNKNOWN = "UNKNOWN"
