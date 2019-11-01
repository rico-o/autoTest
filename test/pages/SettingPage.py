from test.pages.ActivityPage import ActivityPage
from selenium.webdriver.common.by import By
from test.common.FrameOperation import *
import time

class SettingPage(ActivityPage):
    #菜单栏—设置
    def setting(self):
        return self.find_element(By.XPATH,'//*[@id="manage_tree_view"]/ul/li[5]').click()
    #报警短信设置
    def exception_phone_button(self):
        return self.find_element(By.ID,'sos_phone')
    def exception_phone(self):
        return self.exception_phone_button().click()
   #报警类型
    def exception_phone_type(self):
        self.find_element(By.XPATH,'//*[@id="form"]/div[1]/div[2]/div[2]/label/input').click()
        self.find_element(By.XPATH,'//*[@id="form"]/div[1]/div[2]/div[3]/label/input').click()
        self.find_element(By.XPATH,'//*[@id="form"]/div[1]/div[2]/div[4]/label/input').click()
    #报警手机添加
    def exception_phone_add(self):
        self.find_element(By.XPATH, '//*[@id="phones"]').send_keys("13711431756")
        self.find_element(By.ID, 'btnSave').click()
    #关闭按钮
    def close_button(self):
        self.find_element(By.XPATH,'/ html / body / div[3] / span / a[3]').click()
    #路线绘制—设置
    def map_draw_button(self):
        return self.find_element(By.ID,'map_draw')
    def map_draw(self):
        return self.map_draw_button().click()
    #选择轨迹—全选轨迹
    def select_all(self):
        return self.find_element(By.NAME,'btSelectAll').click()
    # 选择轨迹
    def select_track(self):
        return self.find_element(By.XPATH, '// *[ @ id = "form1"] / div[2] / button').click()
    # 选择轨迹—确定
    def confirm(self):
        return self.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/button[1]').click()
    #路线绘制—查看地图
    def map_marker(self):
        return self.find_element(By.ID, 'map_marker').click()
    # 路线绘制—编辑颜色
    def track_edit(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[5]/a[1]').click()
    # 路线绘制—编辑颜色
    def edit_color(self):
        return self.find_element(By.XPATH, '// *[ @ id = "form"] / div[2] / label[3] / input').click()
    #保存按钮
    def save(self):
        return self.find_element(By.ID, 'btnSave').click()
    # 路线绘制表单——查看
    def track_view(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[5]/a[2]').click()
        # 路线绘制表单——删除
    def track_delete(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[5]/a[3]').click()
        # 确定删除按钮
    def delete_confirm_button(self):
        return self.find_element(By.XPATH, '/html/body/div[5]/div[3]/a[1]')
    def delete_confirm(self):
        return self.delete_confirm_button().click()




    # def gpx_file(self):
    #     return self.find_element(By.ID,'gpx_file').send_keys('F:\location\产品测试\自动化测试\\autoTest\data\\130-蓝-GPS_2018-12-20_100440.gpx')




if __name__ == '__main__':
    a = SettingPage()
    a.login()
    a.iframe1()
    a.base_setting()
    a.iframe01()
    a.setting()
    a.iframe0()
    a.exception_phone()
    a.iframeauto()
    a.exception_phone_type()
    a.exception_phone_add()
    a.parentframe()
    a.close_button()
    # a.iframe00()
    # a.defalut_coordinates()
    # a.parentframe()
    # a.iframeauto01()
    # a.defalut_coordinates_add()
    # a.parentframe()
    # a.close_button()
    a.quit_driver()

