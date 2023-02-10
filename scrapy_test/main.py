# -*- coding: utf-8 -*-
# @Time : 2022/11/21 18:27
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:
from scrapy.cmdline import execute
import os

# spider_name = "unity_ads_spider_v3"
spider_name = "google_one"

cmd_string = "scrapy crawl {}".format(spider_name)

if "unity" in spider_name:
    # 垃圾 : VN CA TH MX CN
    # 一般 : RU KR
    # 未测试 : SA,TW,AU,SE
    os.environ.setdefault("ZS_GEO_LIST", "US,JP,RU,KR")
    os.environ.setdefault("ZS_TASK_LIMIT", "50")
    # os.environ.setdefault("ZS_GEO_LIST", "TH")
elif "pinterest" in spider_name:
    cmd_string  += " -a max_request_count=10"


start_cmd = cmd_string.split()

if __name__ == '__main__':
    execute(start_cmd)
