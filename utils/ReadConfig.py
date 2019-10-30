# coding=utf-8


import json


class ReadConfig(object):
    """
    读取配置文件，Excel、josn等文件的读取方法都可写在此类下
    """
    def __init__(self):
        pass

    def read_json(self, json_file):
        """读取json文件"""
        try:
            with open(json_file) as f:
                data = json.load(f)
                return data
        except:
            print("文件不存在或不是json文件")

#一个python的文件有两种使用的方法，第一是直接作为脚本执行，
# 第二是import到其他的python脚本中被调用（模块重用）执行。
# 因此if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
# 在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其他脚本中是不会被执行的。
if __name__ == '__main__':
    data = ReadConfig().read_json("../config/base_data.json")
    print(data)
    print(data['base_url'], data['user_name'], data['password'])
