import unittest
from test.pages.WorkerPage import *


class TestWorkerEdit(unittest.TestCase):
    """工作人员编辑"""
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

    def test_worker_import(self):
        self.worker.worker_edit()
        self.worker.iframe3()
        self.worker.worker_add('修改工作人员','4000000783')





if __name__ == '__main__':
    unittest.main()