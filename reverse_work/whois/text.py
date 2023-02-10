# -*- coding: utf-8 -*-
# @Time : 2023/1/6 15:35
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:

import execjs

def js_from_file(file_name):
    """
    读取js文件
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        result = file.read()

    return result

jsdomstr='''
var jsdom = require('jsdom');
const { JSDOM } = jsdom;
const { window } = new JSDOM();
const { document } = (new JSDOM('')).window;
global.document = document;
var $ = jQuery = require('jquery')(window);
'''

context1 = execjs.compile(jsdomstr + js_from_file("./generatetoken.js"), cwd=r"D:\ALL_workspace\node\node_global\node_modules")

result = context1.call("generateHostKey", "theasay.com")
# result = context1.eval('generateKey()')

print(result)