import unittest
from test.pages.WorkerPage import *


class TestWorkersExport(unittest.TestCase):
    """工作人员导出"""
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

    def test_workers_export(self):
       self.worker.worker_export()



if __name__ == '__main__':
    unittest.main()