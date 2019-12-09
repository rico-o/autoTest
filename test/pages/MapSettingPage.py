from test.pages.ActivityPage import ActivityPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from test.common.WaitUtil import *
import time

class MapSettingPage(ActivityPage,WaitUtil):
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
        self.find_element(By.XPATH, '//*[@id="src_left_up"]').send_keys('23.14707,113.2759')
        self.find_element(By.XPATH, '//*[@id="src_right_down"]').send_keys('23.145817,113.276962')
        self.find_element(By.XPATH, '//*[@id="img_left_up"]').send_keys('23.148362,113.275017')
        self.find_element(By.XPATH, '//*[@id="img_right_down"]').send_keys('23.144609,113.280803')
        self.find_element(By.ID, 'btnSave').click()
    # 默认坐标清除
    def defalut_coordinates_clear(self):
        self.find_element(By.XPATH, '//*[@id="src_left_up"]').clear()
        self.find_element(By.XPATH, '//*[@id="src_right_down"]').clear()
        self.find_element(By.XPATH, '//*[@id="img_left_up"]').clear()
        self.find_element(By.XPATH, '//*[@id="img_right_down"]').clear()
        self.find_element(By.ID, 'btnSave').click()
    #查看地图
    def check_map(self):
        # self.wait.until(EC.text_to_be_present_in_element_value((By.XPATH,"//*[@id='table']/tbody/tr[1]/td[10]/a[1]"),u'查看'))
        # title =EC.title_is('查看')
        # self.visibility_element_located("xpath", "//*[@id='table']/tbody/tr[1]/td[10]/a[1]")
        text =self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[1]").text
        if text=="查看":
            self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[1]").click()
        else:
            time.sleep(60)
            self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[1]").click()
    #上传图片d
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
    def setting(self):
        text = self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[2]").text
        if text == "设置":
            self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[2]").click()
        else:
            time.sleep(10)
            self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[2]").click()
    def setting_error(self):
        try:
            self.find_element(By.CSS_SELECTOR, '#layui-layer4 > div.layui-layer-content')
            print('请保证默认坐标的左上角和右下角坐标有填或者不填')
        except:
            print('设置成功')

    #直播设置
    def live_setting(self):
        text = self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[3]").text
        if text == "设置":
            self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[3]").click()
        else:
            time.sleep(45)
            self.find_element(By.XPATH, "//*[@id='table']/tbody/tr[1]/td[10]/a[3]").click()

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
        return self.find_element(By.XPATH,'//*[@id="form"]/div[5]/button[1]').click()
    def addSign(self):
        return self.addSign_button().click()
    # def addsign(self, name=None, coord=None, radius=None):
    #     self.name_element().send_keys(name)
    #     self.coord_element().send_keys(coord)
    #     self.radius_element().send_keys(radius)
    #     self.find_element(By.ID, 'btnSave').click()
    #签到点——添加
    def select_sign(self):
         self.find_element(By.XPATH,'// *[ @ id = "table"] / thead / tr / th[1] / div[1] / input').click()
         self.find_element(By.XPATH, '  / html / body / div[1] / div / div[3] / button[1]').click()
    # 签到点——编辑
    def sign_edit(self):
        self.find_element(By.XPATH, '// *[ @ id = "sign_table"] / tbody / tr[1] / td[4] / a[1]').click()
    # 编辑签到点
    def sign(self, name=None,  radius=None):
        self.name_element().clear()
        self.radius_element().clear()
        self.name_element().send_keys(name)
        self.radius_element().send_keys(radius)
        self.find_element(By.ID, 'btnSave').click()


    #校准
    def adjustmap(self):
        return  self.find_element(By.XPATH,'// *[ @ id = "box_title"] / form / div[2] / div[3] / a').click()
    # 左上角点取
    def left_choose(self):
        self.find_element(By.XPATH,'//*[@id="set_div"]/div[2]/div/div[2]/div/div[1]/div/input').click()
        container = self.find_element(By.XPATH, '//*[@id="map_container"]/div[1]/div/div[1]/canvas[1]')
        # container_size = container.size
        # print(container_size)
        action = ActionChains(self.driver)
        action.context_click(container)
        action.move_to_element_with_offset(container, 203, 203)
        action.click()
        container_content = self.find_element(By.XPATH, '// *[ @ id = "canvas_content"]')
        action.move_to_element_with_offset(container_content, 50, 50)
        action.click()
        action.perform()
    # 右下角点取
    def right_choose(self):
        self.find_element(By.XPATH, '//*[@id="set_div"]/div[2]/div/div[4]/div/div[1]/div/input').click()
        container = self.find_element(By.XPATH, '//*[@id="map_container"]/div[1]/div/div[1]/canvas[1]')
        action = ActionChains(self.driver)
        action.context_click(container)
        action.move_to_element_with_offset(container, 250, 250)
        action.click()
        container_content = self.find_element(By.XPATH, '// *[ @ id = "canvas_content"]')
        action.move_to_element_with_offset(container_content, 100, 100)
        action.click()
        action.perform()
    #微调
    def adjustmap_second(self):
        return self.find_element(By.XPATH, '/ html / body / div[5] / button').click()
    #通过参数取点
    def map_param(self):
        self.find_element(By.ID, "left_map").send_keys('113.27599,23.147583')
        self.find_element(By.ID,"left_canvas").send_keys('0.165146,0.203360')
        self.find_element(By.ID, "right_map").send_keys('113.278983,23.145491')
        self.find_element(By.ID, "right_canvas").send_keys('0.713607,0.787231')
    #应用
    def save(self):
        return self.find_element(By.XPATH, '/html/body/div[4]/button[2]').click()
    def submit(self):
        return self.find_element(By.ID, 'btnSave').click()
    #添加路程对比
    def addDistance(self):
        return self.find_element(By.XPATH, '//*[@id="form"]/div[3]/button').click()
    def addDistance_name(self):
        return self.find_element(By.ID,'name').send_keys('自动化路程对比')
    #路程按钮
    def distance_button(self):
        return self.find_element(By.XPATH, '// *[ @ id = "distance_table"] / tbody / tr / td[3] / a[2]').click()
    #路程--编辑
    def edit_button(self):
        return self.find_element(By.XPATH, '//*[@id="distance_table"]/tbody/tr/td[3]/a[1]').click()
    #路程--路线按钮
    def distance_select_track_button(self):
        return self.find_element(By.XPATH, ' // *[ @ id = "form1"] / div / button').click()
    # 路程--路线按钮--选择轨迹
    def distance_select_track(self):
        self.find_element(By.XPATH, '//*[@id="table"]/thead/tr/th[1]/div[1]/input').click()
        self.find_element(By.XPATH, '/ html / body / div[1] / div / div[3] / button[1]').click()
    # 路程--路线按钮--设置
    def distance_setting_button(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[7]/a[1]').click()
    # 路程--路线按钮--设置--爬高量/路程坐标
    def distance_setting(self):
        self.find_element(By.ID,'elevation').send_keys('10')
        self.find_element(By.ID, 'coord').send_keys('113.278983,23.145491')
    # 路程--路线按钮--查看
    def distance_check(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[7]/a[2]').click()
    # 路程--路线按钮--删除
    def distance_del(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[7]/a[3]').click()


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

