# coding=utf-8  

from test.pages.LoginPage import LoginPage
import unittest


class TestLogin(unittest.TestCase):
    """登录测试"""

    @classmethod #类方法
    def setUpClass(cls):
        cls.login = LoginPage()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_driver()

    def test_login01(self):
        """登录成功"""
        self.login.login()



if __name__ == '__main__':
    unittest.main()
