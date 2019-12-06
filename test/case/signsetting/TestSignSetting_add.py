from test.pages.signSettingPage import *
import unittest
class Test_Sign_Setting_add(unittest.TestCase):
    """签到点管理——添加签到点和地图叠加测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.setting = signSettingPage()
        cls.setting.login()
        cls.setting.iframe1()
        cls.setting.base_setting()
        cls.setting.iframe01()
        cls.setting.sign_setting()
        cls.setting.iframe0()


    def test_add(self):
        self.setting.map_controls()
        self.setting.sign_choose()
        self.setting.sign_name()


    # @classmethod
    # def tearDownClass(cls):
    #     cls.setting.quit_driver()