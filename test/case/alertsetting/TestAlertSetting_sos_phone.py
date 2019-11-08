import unittest
from test.pages.AlertPage import *
class Test_Setting_phone(unittest.TestCase):
    """报警短信测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = AlertPage()


    def test_exception_phone(self):

            self.setting.login()
            self.setting.iframe1()
            self.setting.base_setting()
            self.setting.iframe01()
            self.setting.alter_setting()
            self.setting.iframe0()
            self.setting.exception_phone()
            self.setting.parentframe()
            self.setting.iframe3()
            self.setting.exception_phone_type()
            self.setting.exception_phone_add()
            self.setting.parentframe()
            self.setting.close_button()



    @classmethod
    def tearDownClass(cls):
        cls.setting.quit_driver()
