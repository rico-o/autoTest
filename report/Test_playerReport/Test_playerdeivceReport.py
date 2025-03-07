# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from test.case.player.TestPlayerDevice import *

import time
if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(TestDeviceImport))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/'+ now +'test_importReport.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
                 stream=fp,
                title="excel运动员批量导入测试",
                 description="excel运动员批量导入自动化测试")
    runner.run(suite)