# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from test.case.worker.TestWorkerImport import *
import time
if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(TestWorkersImport))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/'+ now +'工作人员导入测试报告.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
                 stream=fp,
                title="工作人员导入测试",
                 description="工作人员导入自动化测试")
    runner.run(suite)