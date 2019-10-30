from HTMLTestRunner import HTMLTestRunner

from test.case.player.TestPlayerAdd import *


import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestPlayerAdd('test_add01'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '运动员自动化.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="运动员日期选择器测试",
        description="运动员日期选择器自动化测试")
    runner.run(testunit)
