"""Enum"""
from enum import Enum

class PartnerBrand(Enum):
    """A product may be classified and saved, arrived and pending to
    be classified, marked as a duplicate, failed to be processed, and
    in the midst of processing.

    Args:
        Enum (_type_): state of product
    """
    UNKNOWN = "UNKNOWN"

    @classmethod
    def has_value(cls, value: str) -> bool:
        """
        Checks if the given string value exists within the Enum members' values.

        Args:
            value: The string to check against the Enum values.

        Returns:
            True if the string matches an Enum member's value, False otherwise.
        """
        return value in set(member.value for member in cls)

    @classmethod
    def from_string(cls, value: str):
        """
        Returns the Enum member corresponding to the given string value.
        Raises ValueError if the string does not match any Enum member.
        """
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"'{value}' is not a valid {cls.__name__} status.")