from test.pages.ActivityPage import ActivityPage
from selenium.webdriver.common.by import By
import time
class MapSettingPage(ActivityPage):
    #地图设置
    def map_setting_element(self):
        return self.find_element(By.XPATH,'//*[@id="manage_tree_view"]/ul/li[7]')
    def map_setting(self):
        return self.map_setting_element().click()

    def close_button(self):
        self.find_element(By.XPATH,'/ html / body / div[3] / span / a[3]').click()

    #默认坐标
    def defalut_coordinates_button(self):
        return self.find_element(By.ID,'map_coordinate')
    def defalut_coordinates(self):
        return self.defalut_coordinates_button().click()
    def defalut_coordinates_add(self):
        self.find_element(By.XPATH, '//*[@id="src_left_up"]').send_keys('23.148462,113.27661')
        self.find_element(By.XPATH, '//*[@id="src_right_down"]').send_keys('23.146706,113.279335')
        self.find_element(By.XPATH, '//*[@id="img_left_up"]').send_keys('23.148462,113.27661')
        self.find_element(By.XPATH, '//*[@id="img_right_down"]').send_keys('23.146706,113.279335')
        self.find_element(By.ID, 'btnSave').click()
    # 默认坐标清除
    def defalut_coordinates_clear(self):
        self.find_element(By.XPATH, '//*[@id="src_left_up"]').clear()
        self.find_element(By.XPATH, '//*[@id="src_right_down"]').clear()
        self.find_element(By.XPATH, '//*[@id="img_left_up"]').clear()
        self.find_element(By.XPATH, '//*[@id="img_right_down"]').clear()
        self.find_element(By.ID, 'btnSave').click()

    #上传图片
    def add_map_file(self):
        return self.find_element(By.ID, "add_map_file")
    def add_map(self):
         self.add_map_file().send_keys('C:\\Users\jsb05\Desktop\\bug\\test.jpg')
         time.sleep(5)
    #底图按钮
    def live_map_button(self):
         return self.find_element(By.XPATH, ' // *[ @ id = "box_title"] / form / div[2] / div[4] / a')
    def live_map(self):
        return self.live_map_button().click()
    # 底图
    def upload_img(self):
        self.find_element(By.ID, "upload_img").send_keys('C:\\Users\jsb05\Desktop\\bug\\test.jpg')
        time.sleep(3)
        self.find_element(By.ID, 'btnSave').click()
    # 列表多选框
    def select(self):
        return  self.find_element(By.CSS_SELECTOR,'input:nth-child(1)').click()
    #批量设置
    def settings(self):
        return self.find_element(By.ID,'batchEdit').click()
    #批量删除
    def delete(self):
        return self.find_element(By.XPATH,'//*[@id="box_title"]/form/div[2]/div[2]/a').click()
    # 确定删除按钮
    def delete_confirm_button(self):
        return self.find_element(By.CSS_SELECTOR, '.layui-layer-btn0')
    def delete_confirm(self):
        return self.delete_confirm_button().click()


    #设置
    def setting_button(self):
        return self.find_element(By.XPATH,'//*[@id="table"]/tbody/tr[1]/td[10]/a[1]')
    def setting(self):
        return self.setting_button().click()
    def setting_error(self):
        try:
            self.find_element(By.CSS_SELECTOR, '#layui-layer4 > div.layui-layer-content')
            print('请保证默认坐标的左上角和右下角坐标有填或者不填')
        except:
            print('设置成功')

    #直播设置
    def live_setting_button(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[10]/a[2]')
    def live_setting(self):
        return self.live_setting_button().click()

    # 签到点图片-添加
    def addSignImg_button(self):
        return self.find_element(By.XPATH,'//*[@id="form"]/div[1]/button')
    def addSignImg(self):
        return self.addSignImg_button().click()
    def name_element(self):
        return self.find_element(By.ID,'name')
    def coord_element(self):
        return self.find_element(By.ID,'coord')
    def angle_element(self):
        return self.find_element(By.ID,'angle')
    def radius_element(self):
        return self.find_element(By.ID, 'radius')

    def addsignimg(self, name=None, coord=None, angle=None):
        self.name_element().send_keys(name)
        self.coord_element().send_keys(coord)
        self.angle_element().send_keys(angle)
        self.find_element(By.ID, 'btnSave').click()

    # 签到点图片-添加签到点
    def addSign_button(self):
        return self.find_element(By.XPATH,'//*[@id="form"]/div[5]/button[1]')
    def addSign(self):
        return self.addSign_button().click()
    def addsign(self, name=None, coord=None, radius=None):
        self.name_element().send_keys(name)
        self.coord_element().send_keys(coord)
        self.radius_element().send_keys(radius)
        self.find_element(By.ID, 'btnSave').click()






if __name__ == '__main__':
    a = MapSettingPage()
    a.login()
    a.iframe1()
    a.base_setting()
    a.iframe01()
    a.map_setting()
    a.iframe0()
    a.select()
    a.settings()
    a.parentframe()
    a.iframeauto01()
    a.defalut_coordinates_add()
    # a.add_map()
    # a.defalut_coordinates()
    # a.parentframe()
    # a.iframeauto01()
    # a.defalut_coordinates_add()
    # a.parentframe()
    # a.close_button()
    # a.iframe00()
    # a.live_map()
    # a.parentframe()
    # a.iframeauto01()
    # a.add_live_map()

    # a.exception_phone()
    # a.iframeauto()
    # a.exception_phone_type()
    # a.exception_phone_add()
    # a.parentframe()
    # a.close_button()
    # a.iframe00()
    # a.defalut_coordinates()
    # a.parentframe()
    # a.iframeauto01()
    # a.defalut_coordinates_add()
    # a.parentframe()
    # a.close_button()
    # a.quit_driver()

