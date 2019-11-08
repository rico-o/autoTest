from test.pages.ActivityPage import ActivityPage
from selenium.webdriver.common.by import By
# 菜单栏—轨迹管理
class TrackSettingPage(ActivityPage):
    def track_setting(self):
        return self.find_element(By.XPATH, '//*[@id="manage_tree_view"]/ul/li[8]').click()
    #导入gpx文件
    def gpx_file(self):
        return self.find_element(By.ID, 'gpx_file').send_keys("F:\location\产品测试\自动化测试\\autoTest\data\\130-蓝-GPS_2018-12-20_100440.gpx")
     # 路线绘制表单——删除
    def track_delete(self):
        return self.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[4]/a[2]').click()
     # 确定删除按钮
    def delete_confirm_button(self):
        return self.find_element(By.XPATH, '/html/body/div[3]/div[3]/a[1]')
    def delete_confirm(self):
        return self.delete_confirm_button().click()
     # 轨迹查询
    def gpx_search(self):
         return self.find_element(By.ID, 'name').send_keys("1")
    def search(self):
         return self.find_element(By.ID, 'btnSearch').click()
    def gpx_search_null(self):
        return self.find_element(By.ID, 'name').send_keys("?")
    def search_message(self):
        text = self.find_element(By.XPATH, '// *[ @ id = "table"] / tbody / tr / td').text
        if( text =='没有找到匹配的记录' ):
                print(text)
        else:
                print("查询成功")
        # try:
        #     text = self.find_element(By.XPATH, '// *[ @ id = "table"] / tbody / tr / td').text
        #     if( text =='没有找到匹配的记录' ):
        #         print(text)
        #     else:
        #         print("查询成功")
        # except:
        #     print("查询成功")
if __name__ == '__main__':
    setting = TrackSettingPage()
    setting.login()
    setting.iframe1()
    setting.base_setting()
    setting.iframe01()
    setting.track_setting()
    setting.iframe0()
    setting.gpx_search_null()
    setting.search()
    setting.search_message()





