from test.pages.ActivityPage import ActivityPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# 菜单栏—报警设置
class AlertPage(ActivityPage):
    def alter_setting(self):
        return self.find_element(By.XPATH, '//*[@id="manage_tree_view"]/ul/li[6]').click()
    # 报警短信设置
    def exception_phone_button(self):
        return self.find_element(By.ID, 'sos_phone')
    def exception_phone(self):
        return self.exception_phone_button().click()
    # 报警类型
    def exception_phone_type(self):
        self.find_element(By.XPATH, '//*[@id="form"]/div[1]/div[2]/div[2]/label/input').click()
        self.find_element(By.XPATH, '//*[@id="form"]/div[1]/div[2]/div[3]/label/input').click()
        self.find_element(By.XPATH, '//*[@id="form"]/div[1]/div[2]/div[4]/label/input').click()
    # 报警手机添加
    def exception_phone_add(self):
        self.find_element(By.XPATH, '//*[@id="phones"]').send_keys("13711431756")
        self.find_element(By.ID, 'btnSave').click()
    # 关闭按钮
    def close_button(self):
        self.find_element(By.XPATH, '/ html / body / div[3] / span / a[3]').click()
    #围栏
    def enclosure_area_button(self):
        return self.find_element(By.ID,'enclosure_area')
    def enclosure_area(self):
        return self.enclosure_area_button().click()
    #设置安全围栏
    def safe_area_button(self):
        return self.find_element(By.XPATH,'/ html / body / div / div[2] / div[2] / div[1] / button')
    def safe_area(self):
        return self.safe_area_button().click()
#相对于浏览器xy轴操作
    def chain(self):
        container = self.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[1]/canvas')
        container_size = container.size
        print(container_size)
        action =ActionChains(self.driver)
        action.move_by_offset(950, 100)
        # action.move_by_offset(0, 100)
        action.click()
        action.perform()
    # 相对于画布xy轴操作
    def container_chain(self):
        container = self.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[1]/canvas')
        container_size = container.size
        print(container_size)
        action = ActionChains(self.driver)
        action.context_click(container)
        action.move_to_element_with_offset(container, 100, 100)
        action.click()
        action.move_to_element_with_offset(container, 20, 100)
        action.click()
        action.move_to_element_with_offset(container, 100, 20)
        action.click()
        action.perform()


    #超速报警
    def stretch_zone_button(self):
        return self.find_element(By.ID, 'stretch_zone')
    def stretch_zone(self):
        return self.stretch_zone_button().click()
    # 超时报警
    def time_out_setting_button(self):
        return self.find_element(By.ID, 'time_out_setting')
    def time_out_setting(self):
        return self.time_out_setting_button().click()
        # 选择轨迹—全选轨迹
    #轨迹多选框
    def select_all(self):
        return self.find_element(By.NAME, 'btSelectAll').click()
        # 选择轨迹
    def select_track(self):
        return self.find_element(By.XPATH, '//*[@id="form"]/div[2]/button').click()
    # 选择轨迹—确定
    def confirm(self):
        return self.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/button[1]').click()
      # 路线绘制表单——删除
    def track_delete(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[4]/a[2]').click()
      # 确定删除按钮
    def delete_confirm_button(self):
        return self.find_element(By.XPATH, '/html/body/div[5]/div[3]/a[1]')
    def delete_confirm(self):
        return self.delete_confirm_button().click()
   # 超速表单——编辑
    def track_edit(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[4]/a[1]').click()
    # 超速表单——编辑限定速度
    def track_speed(self):
        return self.find_element(By.NAME, 'speed').send_keys("20")
        # 保存按钮
    #保存
    def save(self):
        return self.find_element(By.ID, 'btnSave').click()
    #下拉菜单开启
    def menu_open(self):
        return self.find_element(By.XPATH,'//*[@id="form"]/div[1]/div/button/span[1]').click()
    #超时报警开启
    def time_out_open(self):
        return self.find_element(By.XPATH, '//*[@id="form"]/div[1]/div/div/ul/li[2]/a').click()
   # 超时报警关闭
    def time_out_close(self):
        return self.find_element(By.XPATH, '  // *[ @ id = "form"] / div[1] / div / div / ul / li[1] / a').click()
    #超时时间——小时
    def activity_time_out_hour(self):
        return self.find_element(By.ID, 'activity_time_out_hour').send_keys('1')
    # 超时时间——分钟
    def activity_time_out_min(self):
        return self.find_element(By.ID, 'activity_time_out_min').send_keys('30')
    # 超时时间——提交
    def submit_form(self):
        return self.find_element(By.ID, 'submit_form').click()





