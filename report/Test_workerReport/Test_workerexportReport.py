# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from test.case.worker.TestWorkerExport import *
import time
if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(TestWorkersExport))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/'+ now +'工作人员导出测试报告.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
                 stream=fp,
                title="工作人员导出测试",
                 description="工作人员导出自动化测试")
    runner.run(suite)