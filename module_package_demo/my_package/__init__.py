"""
My custom package for Python utilities.

This package contains modules for different types of operations.
"""

PACKAGE_VERSION = "0.1.0"

# Import commonly used functions to make them available directly from the package
from .calculations import calculate_circle_area
from .string_utils import reverse_string

# Package metadata
__version__ = PACKAGE_VERSION
__author__ = "Your Name"
