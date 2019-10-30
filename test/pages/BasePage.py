# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


class BasePage(object):
    """基础页面"""

    def __init__(self, driver=None, base_url=None):
        """
         base_url: 默认打开的url，一般都是登录页面
        """
        self.driver = webdriver.Firefox()
        if base_url is None:
            self.base_url = 'https://inside.kanguiji.com/Sys/Login/index'
        else:
            self.base_url = base_url

        # 设置默认打开的页面
        self.open_page()

    def open_page(self):
        """打开默认页面"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(self.base_url)


    def close_page(self):
        """关闭页面"""
        return self.driver.close()

    def quit_driver(self):
        """关闭页面且退出程序"""
        return self.driver.quit()

    def find_element(self, by, element):
        """返回单个定位元素"""
        sleep(1)
        return self.driver.find_element(by, element)

    def find_elements(self, by, element):
        """返回一组定位元素"""
        sleep(1)
        return self.driver.find_elements(by, element)

    def switch_alert(self):
        """返回一组定位元素"""
        sleep(1)
        return self.driver.switch_to.alert

    def log_out(self):
        """退出登录"""
        return self.select_menu("退出登录")
