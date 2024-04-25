# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Project  : will-be-famous
@Time     : 2024/4/19
@Author   : Zhang ZiXu
@Software : PyCharm
@Desc     :  
@Last Modify          @Version        @Author
---------------       --------        -----------
2024/4/19               1.0             Zhang ZiXu
"""
import subprocess
from urllib import parse

import execjs
import requests


# import os
# os.environ["PYTHONIOENCODING"] = "utf-8"

def set_params():
    """设置请求的参数"""
    params = {
        'pageNum': 1,
        'pageSize': 10,
        'keyword': '',
        'city1': '',
        'type': '少儿类|教育类|文艺类|社科类|科技类|综合类|美术类|电子|音像|音像电子|大学类|古籍类',
        'group': '',
        't': "pdc,ele"
    }
    return parse.urlencode(params, safe='&,')


def send_request(params):
    """发送请求到API"""
    url = "https://pdc.capub.cn/api/publisher/publisherVagueStatList"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, data=params, headers=headers)
    return response


def run_js(script_path, input_data):
    result = subprocess.run(
        ['node', script_path, input_data],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    if result.stderr:
        print("Error:", result.stderr)
    return result.stdout


# 使用这个函数来运行你的 JavaScript 脚本
output = run_js("demo.js", "some input data")
if __name__ == '__main__':
    data = send_request(set_params()).json()["result"]
    print(run_js("demo.js", data))
    # js_code = open("demo.js", "r", encoding="utf-8").read()
    # ctx = execjs.compile(js_code)
    # print(ctx.call('decryptResult', data))
