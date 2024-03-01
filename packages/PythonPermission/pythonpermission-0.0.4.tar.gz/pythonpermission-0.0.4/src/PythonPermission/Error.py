"""
This module is a collection of errors that are used in the PythonPermission module

LICENSE: All rights reserved
"""


class PrivateFunctionError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
