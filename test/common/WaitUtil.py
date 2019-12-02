
from selenium.webdriver.support import expected_conditions as EC

from test.pages.BasePage import *

class WaitUtil(BasePage):
    def presence_of_element_located(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
        :param locatorMethod:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            if locationType.lower() in self.locationTypeDict:
                # if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(
                    EC.presence_of_element_located((
                        self.locationTypeDict[locationType.lower()], locatorExpression)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e


    def frame_to_be_available_and_switch_to_it(self, locationType, locatorExpression, *args):
        """
        检查frame是否存在，存在则切换进去
        :param locationType:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((
                    self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception as e:
            # 抛出异常信息给上层调用者
            raise e

    def visibility_element_located(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素的出现
        :param locationType:
        :param locatorExpression:
        :param arg:
        :return:
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((self.locationTypeDict[locationType.lower()], locatorExpression)))
            return element
        except Exception as e:
            raise e
