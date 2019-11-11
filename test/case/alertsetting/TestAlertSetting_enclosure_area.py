from test.pages.AlertPage import *
import unittest
class Test_Setting_area(unittest.TestCase):
    """超速报警——选择轨迹测试"""

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
        self.setting.enclosure_area()
        self.setting.iframe3()
        self.setting.safe_area()
        # 相对于浏览器xy轴操作
        # self.setting.chain()
        # 相对于画布xy轴操作
        self.setting.container_chain()

        # self.setting.iframe4()
        # self.setting.select_all()
        # self.setting.confirm()

    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.setting.quit_driver()