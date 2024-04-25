# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Project  : will-be-famous
@Time     : 2024/4/16
@Author   : Zhang ZiXu
@Software : PyCharm
@Desc     :  
@Last Modify          @Version        @Author
---------------       --------        -----------
2024/4/16               1.0             Zhang ZiXu
"""
import execjs

js_code = open("demo.js", "r", encoding="utf-8").read()
# print(js_code)
ctx = execjs.compile(js_code)
result = ctx.call('main123', '14759F5D2953E25AD70B2BCED66A19656461CFFC')

print(result)

result2 = ctx.call("f")
print(result2)

print(execjs.eval("new Date"))
