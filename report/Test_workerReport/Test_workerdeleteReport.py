from HTMLTestRunner import HTMLTestRunner

from test.case.worker.TestWorkerDelete import *
from test.case.worker.TestWorkerDeletes import *

import time
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestWorker_delete('test_worker_delete'))
    testunit.addTest(TestWorker_deletes('test_worker_deletes'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = 'F:/location/产品测试/自动化测试/测试报告/' + now + '工作人员自动化.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title="工作人员删除测试",
        description="工作人员删除测试")
    runner.run(testunit)
