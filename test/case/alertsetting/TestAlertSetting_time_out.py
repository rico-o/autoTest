from test.pages.AlertPage import *
import unittest
class Test_Setting_time_out_setting(unittest.TestCase):
    """超时报警——开启测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = AlertPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.alter_setting()
        cls.setting.iframe0()


    def test_select_track(self):
        self.setting.time_out_setting()
        self.setting.iframe3()
        self.setting.menu_open()
        self.setting.time_out_open()
        self.setting.activity_time_out_hour()
        self.setting.activity_time_out_min()
        self.setting.submit_form()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
