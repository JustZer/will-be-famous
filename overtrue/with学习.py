# -*- coding: utf-8 -*-
# @Time : 2023/1/12 10:11
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:

import redis
redis_conn = redis.StrictRedis()

str_list = [
    "1",
    "1",
    "1",
    "1",
    "1",
    "1",
    "1",
    "1",
    "1",
    "1",
    "1"
]

with open(r"C:\Users\Simon\Desktop\work_test.txt", "r") as f:
    content = f.read()

content = content.split("\n")
print(type(content))
print(content[0])


for text in content:
    redis_conn.lpush("ECOMM:FN:V1:ALIEXPRESS:CATEGORY:PRODCUT:CRAWL:QUEUE", text)
