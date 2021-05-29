# -*- coding: utf-8 -*-
# @Time : 2021/5/29 2:27 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : uf03_test_multi_method_cases.py
import unittest

# import To_be_tested class
from apiAssurance.unittest_flow.uf01_to_be_tested import MathMethod, MultiMethod


class TestMultiMethod(unittest.TestCase):
    """in this class every class is a testcase"""

    def test_two_positive_multi(self):
        """as it's name saying"""
        res_4 = MultiMethod(1, 2).multi_function()
        self.assertEqual(2, res_4, "test two positive multi")

    def test_two_negative_multi(self):
        """as it's name saying"""
        res_5 = MultiMethod(-1, -2).multi_function()
        self.assertEqual(2, res_5, "test two negative multi")

    def test_two_zero_multi(self):
        """as it's name saying"""
        res_6 = MultiMethod(0, 0).multi_function()
        self.assertEqual(0, res_6, "test two zero multi")
