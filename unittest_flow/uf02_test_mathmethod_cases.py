# -*- coding: utf-8 -*-
# @Time : 2021/5/29 2:11 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : uf02_test_mathmethod_cases.py

import unittest

# import To_be_tested class
from apiAssurance.unittest_flow.uf01_to_be_tested import MathMethod, MultiMethod


class TestMathMethod(unittest.TestCase):
    """in this class every class is a testcase"""

    def test_two_positive_plus(self):
        """as it's name saying"""
        # GIVEN - WHEN -THEN
        res_1 = MathMethod(1, 2).add_function()
        self.assertEqual(3, res_1, "test two positive add")

    def test_two_negative_plus(self):
        """as it's name saying"""
        # GIVEN - WHEN -THEN
        res_2 = MathMethod(-1, -2).add_function()
        self.assertEqual(-3, res_2, "test two negative add")

    def test_two_zero_plus(self):
        """as it's name saying"""
        # GIVEN - WHEN -THEN
        res_1 = MathMethod(0, 0).add_function()
        self.assertEqual(0, res_1, "test two zero add")





