import unittest
import os


def discover_case(case_dir):
    # 待执行用例的目录
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="*.py", top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            print(test_case)
            # 添加用例到testcase
            # testcase.addTests(test_case)
            testcase.addTests(test_case)

    return (testcase)


path = './test/case'
case = discover_case(case_dir=path)
print(case)
