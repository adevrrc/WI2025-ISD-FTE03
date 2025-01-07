"""This module defines the Department enumeration.

Example:
    >>> print(Department.COMPUTER_SCIENCE)
    >>> Department.COMPUTER_SCIENCE
"""

__author__ = "COMP-2327 Faculty"
__version__ = "1.1.2025"

from enum import Enum, auto

class Department(Enum):
    """Represents departments within a post-secondary institution."""
    
    COMPUTER_SCIENCE = auto()
    """The computer science department."""

    EDUCATION = auto()
    """The education department."""    
    
    ENGINEERING = auto()
    """The engineering department."""
    
    MEDICINE = auto()
    """The medicine department."""
