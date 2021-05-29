# -*- coding: utf-8 -*-
# @Time : 2021/5/29 2:37 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : uf05_testrunner_generate_report.py
import unittest

from apiAssurance.unittest_flow.uf04_testsuite_for_module_uf01 import \
    suite_for_MathMethodModule, suite_for_MultiMethodModule


def run_tests():
    with open("TestReport.html", "w") as file:
        runner = unittest.TextTestRunner(stream=file,
                                         verbosity=2,
                                         descriptions="just for unitest",
                                         )

        runner.run(suite_for_MathMethodModule)

