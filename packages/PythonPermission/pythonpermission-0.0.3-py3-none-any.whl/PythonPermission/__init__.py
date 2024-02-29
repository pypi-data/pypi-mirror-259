"""
PythonPermission is a package that provides a way to create private, fileprivate, and protected functions in Python.

LICENSE: All rights reserved
"""

from .Error import PrivateFunctionError
from .Attribute import private, fileprivate, protected, internal


__all__ = ["private", "fileprivate", "protected", "internal", "PrivateFunctionError"]
__author__ = "Maxland255"
__version__ = "0.0.3"
__license__ = "GNU GPLv3"
