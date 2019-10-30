import time
import win32api
import win32con
import pyperclip
class  UpLoad_File(object):
    def UpLoad_File(self, filePath):
        """
        使用 python 的 win32api，win32con 模拟按键输入，实现文件上传操作。
        :param webEle: 页面中的上传文件按钮,是已经获取到的对象
        :param filePath: 要上传的文件地址，绝对路径。如：D:\\timg (1).jpg
        :param check_Input:检查input标签中是否有值 #仅用来检查，在return 处调用一次，多余可删除
        :return: 成功返回：上传文件后的地址，失败返回：""
        """

        pyperclip.copy(filePath)  # 复制文件路径到剪切板
        # webEle.click()  # 点击上传图片按钮
        time.sleep(3)  # 等待程序加载 时间 看你电脑的速度 单位(秒)
        # 发送 ctrl（17） + V（86）按钮
        win32api.keybd_event(17, 0, 0, 0)
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(2)
        win32api.keybd_event(13, 0, 0, 0)  # (回车)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键