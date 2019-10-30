# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from test.case.player.TestPlayerEdit import *
import time
if __name__ == '__main__':

    suite = unittest.TestSuite(unittest.makeSuite(TestPlayerEdit))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/'+ now +'运动员编辑.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
                 stream=fp,
                title="运动员编辑测试",
                 description="运动员编辑自动化测试")
    runner.run(suite)
