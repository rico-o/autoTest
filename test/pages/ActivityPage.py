# coding=utf-8

from test.pages.LoginPage import LoginPage
from time import sleep
from selenium.webdriver.common.by import By
from test.common.FrameOperation import *
from test.common.Upload_File import *
import re

class ActivityPage(LoginPage, FrameOperation ,UpLoad_File):


    def base_setting(self):
        return self.base_setting_element().click()


    def base_setting_element(self):
        """基本设置"""
        #range(start, stop[, step])
       # start,默认是从 0 开始。
       # stop计数到 stop 结束，不包括 stop。
       # 步长，默认为1。

        for i in range(1,100):
            # print(i)
            a= self.find_element(By.XPATH, "//*[@id='table']/tbody/tr["+str(i)+"]/td[2]").text

            if re.search('测试', a):
                print(a)
                b = self.find_element(By.XPATH, "//*[@id='table']/tbody/tr["+str(i)+"]/td[4]/a[2]")
                break
            else:
                pass
        return b


if __name__ == '__main__':
    a =ActivityPage()
    a.login()
    a.iframe1()
    # a.base_element()
    # # a.base_setting01()
    a.base_setting()
    # sleep(3)










