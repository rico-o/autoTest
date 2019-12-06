from test.pages.ActivityPage import ActivityPage
from selenium.webdriver.common.by import By
import time

class WorkerPage(ActivityPage):
    #工作人员-菜单栏
    def worker(self):
        return self.find_element(By.XPATH,'//*[@id="manage_tree_view"]/ul/li[3]').click()
    #工作人员—添加按钮
    def add_button(self):
        return self.find_element(By.XPATH, '//*[@id="form"]/div[2]/a').click()

    def worker_name_element(self):
        return self.find_element(By.ID, 'name')
    def worker_device_id_elemtnt(self):
        return  self.find_element(By.ID,'device_id')

    # 工作人员—手动输入添加
    def worker_add(self,worker_name,device_id):
        self.worker_name_element().send_keys(worker_name)
        self.worker_device_id_elemtnt().send_keys(device_id)
        self.find_element(By.ID, 'btnSave').click()

    # 工作人员—读取excel添加
    def worker_add01(self, worker_name,device_id):
        if worker_name != None:
            worker_name_element = self.find_element(By.ID, 'name')
            worker_name_element.send_keys(worker_name)
        if device_id != None:
            device_id_element = self.find_element(By.ID, 'device_id')
            device_id_element.send_keys(device_id)

        self.find_element(By.ID, 'btnSave').click()


    #导入
    def worker_import_button(self):
        return self.find_element(By.XPATH,'// *[ @ id = "form"] / div[3] / a[1]')
    def worker_import(self):
        return self.worker_import_button().click()

    # 导出
    def worker_export_button(self):
        return self.find_element(By.ID, 'out')
    def worker_export(self):
        return self.worker_export_button().click()

        # 工作人员导入错误提示
    def error_message_import(self):
        self.find_element(By.CLASS_NAME, 'layui-layer-content').click()
        print('excel或者赛事已经存在相同的姓名/已经发给过其他工作人员,未能导入成功。')

   #工作人员多选栏
    def worker_select_all_button(self):
        return self.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
    def worker_select_all(self):
        return self.worker_select_all_button().click()
 #批量工作人员删除
    def workers_deletes_button(self):
        return  self.find_element(By.CSS_SELECTOR,'#form > div.row > div > div > a')
    def  workers_deletes(self):
        return self.workers_deletes_button().click()

    # 工作人员删除
    def workers_delete_button(self):
        return self.find_element(By.XPATH, '// *[ @ id = "table"] / tbody / tr[1] / td[5] / a[2]')
    def workers_delete(self):
        return self.workers_delete_button().click()
#工作人员删除-确定按钮
    def confirm_button(self):
       return self.find_element(By.XPATH,'// *[ @ id = "layui-layer1"] / div[3] / a[1]')
    def confirm(self):
        return self.confirm_button().click()
    def confirm01(self):
        return self.find_element(By.XPATH,'// *[ @ id = "layui-layer3"] / div[3] / a[1]').click()

    #工作人员-编辑
    def worker_edit_button(self):
        return self.find_element(By.XPATH,'//*[@id="table"]/tbody/tr[3]/td[5]/a[1]')
    def worker_edit(self):
        return self.worker_edit_button().click()



if __name__ == '__main__':


        b = WorkerPage()
        b.login()
        b.iframe1()
        b.base_setting()
        b.iframe01()
        b.worker()
        b.iframe0()
        b.worker_select_all()
        b.workers_delete()
        b.confirm()


        # b.add_button()
        # b.iframeauto()
        # b.worker_add('gg','4000000119')
        # b.quit_driver()
        # b.worker_import()
        # b.UpLoad_File('F:\location\产品测试\自动化测试\\autoTest\data\\1.13直播测试2019-10-25 16_26_46.xlsx')




