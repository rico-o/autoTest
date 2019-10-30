from test.pages.WorkerPage import *
import unittest
from test.common.Common import *

class TestWorker_delete(unittest.TestCase):
    """工作人员删除"""
    @classmethod  # 类方法
    def setUpClass(cls):
        cls.worker = WorkerPage()
        cls.worker.login()
        cls.worker.iframe1()
        cls.worker.base_setting()
        cls.worker.iframe01()
        cls.worker.worker()
        cls.worker.iframe0()

    @classmethod  # 类方法
    def tearDownClass(cls):
        cls.worker.quit_driver()

    def test_worker_delete(self):
        self.worker.workers_delete()
        self.worker.parentframe()
        self.worker.confirm01()


if __name__ == '__main__':
    unittest.main()