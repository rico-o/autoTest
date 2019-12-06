from test.pages.ActivityPage import ActivityPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class signSettingPage(ActivityPage):
    #菜单栏—签到点管理
    def sign_setting(self):
        return self.find_element(By.XPATH,'//*[@id="manage_tree_view"]/ul/li[9]').click()
    #添加签到点
    def sign_choose(self):
        self.find_element(By.ID, 'add_sign').click()
        container = self.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[1]/canvas')
        action = ActionChains(self.driver)
        action.context_click(container)
        action.move_to_element_with_offset(container, 1000, 800)
        action.click()
        action.perform()
    #地图叠加图片选择
    def map_controls(self):
        self.find_element(By.XPATH,'/ html / body / div / div[2] / div[2] / div[1] / div / button / span[1]').click()
        self.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div/ul/li[2]/a/span[1]').click()
    #签到点名称
    def sign_name(self):
         self.find_element(By.ID, 'small_option_input').send_keys("111")
         self.find_element(By.XPATH, '//*[@id="option_row"]/div/button[1]').click()
