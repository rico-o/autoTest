# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# import os
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """基础页面"""

    def __init__(self, driver=None, base_url=None,test_url=None):
        """
         base_url: 默认打开的url，一般都是登录页面
        """
        self.driver = webdriver.Firefox()
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css_selector": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }
        self.wait = WebDriverWait(self.driver, 60)
     #
     # #正式服
     #    if base_url is None:
     #        self.base_url = 'https://manage.kanguiji.com/Sys/Login/index'
     #    else:
     #        self.base_url = base_url
    # 测试服
        if test_url is None:
            self.base_url = 'https://inside.kanguiji.com/Sys/Login/index'
        else:
            self.test_url = test_url

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



