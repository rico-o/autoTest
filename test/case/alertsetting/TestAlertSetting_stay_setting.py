from test.pages.AlertPage import *
import unittest
class Test_Setting_stay_setting(unittest.TestCase):
    """停留报警——开启测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = AlertPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.alter_setting()
        cls.setting.iframe0()


    def test_stay_setting(self):
        self.setting.stay_setting()
        self.setting.iframe3()
        self.setting.stay_setting_open()
        self.setting.stay_sec()
        self.setting.submit_form()


    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
