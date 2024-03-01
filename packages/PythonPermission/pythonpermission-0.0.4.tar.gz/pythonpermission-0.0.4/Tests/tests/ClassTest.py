"""
This file contains the tests for the PythonPermission module

LICENSE: All rights reserved
"""
from PythonPermission import *


class PrivateInit:
    @private()
    def __init__(self):
        pass

    @classmethod
    def test(cls):
        return cls()


class FilePrivateInit:
    @fileprivate()
    def __init__(self):
        pass

    @classmethod
    def test(cls):
        return cls()


class ProtectedInit:
    @protected()
    def __init__(self):
        pass

    @classmethod
    def test(cls):
        return cls()


class Protected2(ProtectedInit):
    def __init__(self):
        super().__init__()


class InternalInit:
    @internal()
    def __init__(self):
        pass

    @classmethod
    def test(cls):
        return cls()


class MethodeTest:
    @private()
    def private_methode(self):
        return "private"

    @fileprivate()
    def fileprivate_methode(self):
        return "fileprivate"

    @protected()
    def protected_methode(self):
        return "protected"

    @internal()
    def internal_methode(self):
        return "internal"


@private()
class PrivateClass:
    pass


@fileprivate()
class FilePrivateClass:
    pass


@protected()
class ProtectedClass:
    pass


@internal()
class InternalClass:
    pass
