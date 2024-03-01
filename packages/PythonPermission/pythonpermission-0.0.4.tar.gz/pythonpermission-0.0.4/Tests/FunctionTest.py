"""
This file contains the tests for the PythonPermission module

LICENSE: All rights reserved
"""

from PythonPermission import *


@private()
def test_private():
    return "private"


@fileprivate()
def test_fileprivate():
    return "fileprivate"


@protected()
def test_protected():
    return "protected"


@internal()
def test_internal():
    return "internal"
