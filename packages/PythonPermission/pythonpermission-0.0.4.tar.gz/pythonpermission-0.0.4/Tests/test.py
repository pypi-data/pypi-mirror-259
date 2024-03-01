"""
This file contains the tests for the PythonPermission module

LICENSE: All rights reserved
"""
import sys
sys.path.append("./src")

from unittest import TestCase, main
from PythonPermission import PrivateFunctionError

from tests.ClassTest import PrivateClass, FilePrivateClass, ProtectedClass, \
    PrivateInit, FilePrivateInit, ProtectedInit, Protected2, MethodeTest
from FunctionTest import test_private, test_fileprivate, test_protected


class Test(TestCase):
    def test_class_private_init(self):
        with self.assertRaises(PrivateFunctionError):
            PrivateInit()

        assert isinstance(PrivateInit.test(), PrivateInit)

    def test_class_file_private_init(self):
        with self.assertRaises(PrivateFunctionError):
            FilePrivateInit()

        assert isinstance(FilePrivateInit.test(), FilePrivateInit)

    def test_class_protected_init(self):
        with self.assertRaises(PrivateFunctionError):
            ProtectedInit()

        assert isinstance(ProtectedInit.test(), ProtectedInit)
        assert isinstance(Protected2(), Protected2)

    # @skip("Internal function does not support test")
    # def test_class_internal_init(self):
    #     try:
    #         assert isinstance(InternalInit(), InternalInit)
    #         assert isinstance(InternalInit.test(), InternalInit)
    #     except AttributeError:
    #         self.skipTest("InternalInit has an exception")

    def test_class_methode(self):
        with self.assertRaises(PrivateFunctionError):
            MethodeTest().private_methode()

        with self.assertRaises(PrivateFunctionError):
            MethodeTest().fileprivate_methode()

        with self.assertRaises(PrivateFunctionError):
            MethodeTest().protected_methode()

        # try:
        #     assert MethodeTest().internal_methode() == "internal"
        # except AttributeError:
        #     self.skipTest("MethodeTest internal methode has an exception")

    def test_class_private(self):
        with self.assertRaises(PrivateFunctionError):
            PrivateClass()

    def test_class_file_private(self):
        with self.assertRaises(PrivateFunctionError):
            FilePrivateClass()

    def test_class_protected(self):
        with self.assertRaises(PrivateFunctionError):
            ProtectedClass()

    # @skip("Internal function does not support test")
    # def test_class_internal(self):
    #     try:
    #         assert isinstance(InternalClass(), type(InternalClass))
    #     except AttributeError:
    #         self.skipTest("InternalClass has an exception")

    def test_function_private(self):
        with self.assertRaises(PrivateFunctionError):
            test_private()

    def test_function_file_private(self):
        with self.assertRaises(PrivateFunctionError):
            test_fileprivate()

    def test_function_protected(self):
        with self.assertRaises(PrivateFunctionError):
            test_protected()

    # @skip("Internal function does not support test")
    # def test_function_internal(self):
    #     try:
    #         assert test_internal() == "internal"
    #     except AttributeError:
    #         self.skipTest("test_internal has an exception")


if __name__ == "__main__":
    main()
