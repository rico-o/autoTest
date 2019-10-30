# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from test.case.player.TestPlayerSerach import *
import time
if __name__ == '__main__':

    suite = unittest.TestSuite(unittest.makeSuite(TestSearch))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/'+ now +'testserach.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
                 stream=fp,
                title="运动员查询测试",
                 description="运动员查询自动化测试")
    runner.run(suite)
