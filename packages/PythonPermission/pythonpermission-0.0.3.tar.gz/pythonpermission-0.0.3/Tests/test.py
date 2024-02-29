"""
This file contains the tests for the PythonPermission module

LICENSE: All rights reserved
"""
from src.PythonPermission import *
# from tests.Test2 import test2


# class Test:
#     @private()
#     def __init__(self, value: int, message: str):
#         self.__value = value
#         self.__message = message
#
#     @classmethod
#     @fileprivate()
#     def from_file(cls, value: int) -> "Test":
#         return cls(value, "This an error message")
#
#
# @internal()
# def test() -> None:
#     pass


class Test:
    @private()
    def private_test(self):
        pass

    @fileprivate()
    def fileprivate_test(self):
        pass

    @internal()
    def internal_test(self):
        pass

    @protected()
    def protected_test(self):
        pass


if __name__ == "__main__":
    # t1 = Test(5, "This is a tests")
    # t2 = Test.from_file(5)

    # test()
    # test2()

    # src.PythonPermission.test()

    t = Test()

    t.private_test()
    t.fileprivate_test()
    t.internal_test()
    t.protected_test()
