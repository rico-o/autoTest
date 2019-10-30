
import unittest
from HTMLTestRunner import HTMLTestRunner
from test.case.player.TestPlayImgsDelete import *
import time

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(TestPlayerImgs_delete))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + 'test_playerdelete.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="运动员图片批量删除测试",
        description="运动员图片删除自动化测试")
    runner.run(suite)