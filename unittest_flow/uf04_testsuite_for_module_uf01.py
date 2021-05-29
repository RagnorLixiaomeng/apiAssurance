# -*- coding: utf-8 -*-
# @Time : 2021/5/29 2:28 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : uf04_testsuite_for_module_uf01.py


import unittest

from apiAssurance.unittest_flow.uf02_test_mathmethod_cases import TestMathMethod
from apiAssurance.unittest_flow.uf03_test_multi_method_cases import TestMultiMethod

"""test suite 1: for module uf02:optional cases"""
suite_for_MathMethodModule = unittest.TestSuite()
suite_for_MathMethodModule.addTests([
                                    TestMathMethod("test_two_positive_plus"),
                                    TestMathMethod("test_two_negative_plus"),
                                    TestMathMethod("test_two_zero_plus")
                                    ])


"""test suite 2: for module uf03"""
suite_for_MultiMethodModule = unittest.TestSuite()
suite_for_MultiMethodModule.addTest(unittest.TestLoader().loadTestsFromModule(TestMultiMethod))
