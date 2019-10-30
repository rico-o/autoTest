# coding=utf-8

from test.pages.BasePage import BasePage
from utils.ReadConfig import ReadConfig
from selenium.webdriver.common.by import By
import os

class LoginPage(BasePage):
    """登录页面"""

    def user_name_element(self):
        """账号"""
        return self.find_element(By.ID, "user_name")

    def password_element(self):
        """密码"""
        return self.find_element(By.ID, "password_text")

    def login_button(self):
        """登录按钮"""
        return self.find_element(By.ID, "submit")


    def login_fail_element(self):
        """登录失败"""
        return self.switch_alert()

    def login(self, user_name=None, password=None):
        """登录操作"""
        account_user_name, account_password = self.get_account()

        if user_name is None:
            user_name = account_user_name
        else:
            user_name = user_name

        if password is None:
            password = account_password

        self.user_name_element().send_keys(user_name)
        self.password_element().send_keys(password)
        self.login_button().click()

    @staticmethod
    def get_account():
        """获取测试账号和密码"""
        current_path = os.path.abspath(os.path.dirname(__file__))
        json_path = current_path + '/../../config/base_data.json'
        account = ReadConfig().read_json(json_path)
        return account['user_name'], account['password']


if __name__ == '__main__':
    a = LoginPage()
    a.login()
    # a.quit_driver()
