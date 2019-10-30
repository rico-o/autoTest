from test.pages.WorkerPage import *
import unittest
from test.common.Common import *

class TestWorker_deletes(unittest.TestCase):
    """工作人员批量删除"""
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

    def test_worker_deletes(self):
        self.worker.worker_select_all()
        self.worker.workers_deletes()
        self.worker.confirm()


if __name__ == '__main__':
    unittest.main()