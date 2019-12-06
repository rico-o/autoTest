# coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
from test.case.TestLogin import *
import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestLogin('test_login01'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/'+ now +'testlogin.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
                 stream=fp,
                title="登录测试",
                 description="登录自动化测试")
    runner.run(testunit)