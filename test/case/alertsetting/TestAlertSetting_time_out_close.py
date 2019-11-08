from test.pages.AlertPage import *
import unittest
class Test_Setting_time_out_setting_close(unittest.TestCase):
    """超时报警——关闭测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = AlertPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.alter_setting()
        cls.setting.iframe0()


    def test_time_out_delete(self):
        self.setting.time_out_setting()
        self.setting.iframe3()
        self.setting.menu_open()
        self.setting.time_out_close()
        self.setting.submit_form()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
