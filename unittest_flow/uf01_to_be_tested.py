# -*- coding: utf-8 -*-
# @Time : 2021/5/29 2:07 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : uf01_to_be_tested.py

"""
used to afford To-be-tested

"""


class MathMethod(object):
    """+ - """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_function(self):
        return self.a + self.b

    def minus_function(self):
        return self.a - self.b


class MultiMethod(object):
    """* /"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multi_function(self):
        return self.num1 * self.num2

    def divide_function(self):
        return self.num1 / self.num2
