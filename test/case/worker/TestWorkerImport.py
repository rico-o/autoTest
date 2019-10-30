import unittest
from test.pages.WorkerPage import *


class TestWorkersImport(unittest.TestCase):
    """工作人员导入"""
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

    def test_workers_import(self):
       self.worker.worker_import()
       self.worker.UpLoad_File('F:\location\产品测试\自动化测试\\autoTest\data\\工作人员导入测试.xlsx')
       self.worker.parentframe()
       try:
           self.worker.error_message_import()
       except:
           print('导入成功')



if __name__ == '__main__':
    unittest.main()