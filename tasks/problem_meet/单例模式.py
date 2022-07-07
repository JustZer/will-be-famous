# -*- coding: utf-8 -*-
# @Time : 2022/5/27 10:40
# @Author : Zhangzixu
# @Software: PyCharm
# @Description: 创建的方式在不断的初始化一个类,而初始化的类会去读取一个比较大的 JSON 文件,导致多次调用的情况下内存占用很大,影响程序执行速率
import json

import redis


class ReadFile:
    _instance = None

    # 解决方法2:使用__new__魔法方法来控制实例的创建过程
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ReadFile, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.red_conn = redis.StrictRedis(host="127.0.0.1", port=6379)

    def read_big_file(self):
        f = self.red_conn.get("super_big_json_file")
        j = json.load(f)
        return j


class RunPython:
    # 解决方法1: 给类添加初始化方法,让需要用到的方法只初始化一次,它的内容就被放到了内存中,直接调用即可
    def __init__(self):
        self.big_file = ReadFile().read_big_file()

    # 错误样例
    def run(self):
        # 这就是问题所在,ReadFile类在这里被疯狂初始化,如果RunPython的run方法被执行500次,那么ReadFile类就会被初始化500次,极大的浪费计算机资源
        if 'xxx' in ReadFile().read_big_file():
            print("xxx")

    # 解决方法1
    def fix1(self):
        if 'xxx' in self.big_file:
            print("fix1")


# 解决方法3:使用装饰器,效果跟方法2是一样的,就是单独领出来了而已
from functools import wraps


def singleton(cls):
    _instances = {}

    @wraps(cls)
    def get_instances(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instances()


if __name__ == '__main__':
    # 方法2 样例
    one = ReadFile()
    two = ReadFile()
    print(f"one:{id(one)},two:{id(two)}")
    print(one == two, one is two)
