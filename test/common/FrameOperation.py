# coding=utf-8
from test.common.Common import *


class FrameOperation(object):
    """表格操作"""

    def __init__(self, driver):
        self.driver = driver


    def iframe1(self):
        self.default = self.driver.switch_to.default_content()
        self.iframe1 = self.driver.switch_to.frame('iframe1')

    def iframe0(self):
        self.default = self.driver.switch_to.default_content()
        self.iframe1 = self.driver.switch_to.frame('iframe1')
        self.iframe0 = self.driver.switch_to.frame('iframe0')
    def iframe01(self):
    #两个frame1同名
        self.parent = self.driver.switch_to.parent_frame()
        self.iframe1 = self.driver.switch_to.frame('iframe1')


    def iframeauto(self):
        self.default = self.driver.switch_to.default_content()
        self.iframe1 = self.driver.switch_to.frame('iframe1')
        self.iframeauto = self.driver.switch_to.frame('layui-layer' + get_last_id())

    def iframe2(self):
        self.default = self.driver.switch_to.default_content()
        self.iframe1 = self.driver.switch_to.frame('iframe1')
        self.iframeauto = self.driver.switch_to.frame('layui-layer-iframe2')

    def iframe3(self):
        self.default = self.driver.switch_to.default_content()
        self.iframe1 = self.driver.switch_to.frame('iframe1')
        self.iframeauto = self.driver.switch_to.frame('layui-layer-iframe3')

    def iframe4(self):
        self.parent = self.driver.switch_to.parent_frame()
        self.iframeauto = self.driver.switch_to.frame('layui-layer-iframe4')

    def parentframe(self):
        self.parent = self.driver.switch_to.parent_frame()
    def iframe00(self):
        self.iframe0 = self.driver.switch_to.frame('iframe0')
    def iframeauto01(self):
        self.iframeauto = self.driver.switch_to.frame('layui-layer-iframe' + get_last_id())
