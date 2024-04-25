# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Project  : will-be-famous
@Time     : 2024/4/12
@Author   : Zhang ZiXu
@Software : PyCharm
@Desc     : 雪球网 OB 混洗处理
@Last Modify          @Version        @Author
---------------       --------        -----------
2024/4/12               1.0             Zhang ZiXu
"""

import requests

url = "https://xueqiu.com/statuses/livenews/list.json?count=15&max_id="

payload = {}
headers = {
    'Cookie':
        'acw_tc=2760779817129106667853685ebf7be45ec56e4ff25dc3a4c60bc9b22cb668; '
        'xq_a_token=4b8bc7136c9fd7b4395f9ca0a65c38363243df2b; '
        # 'xqat=4b8bc7136c9fd7b4395f9ca0a65c38363243df2b; '
        # 'xq_r_token=3f230866347670b258c76aecd81456e63e6aa98b; '
        # 'xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxNDk1NjQ2MiwiY3RtIjoxNzEyOTEwNjIwNjA3LCJjaWQiOiJkOWQwbjRBWnVwIn0.FBILLk-NDGTDGtTI4TcVXCXmG2aCzL4tbH8fdG2ubUcW24ms2tRIP3fMP-hhSu0yBuXN5OcymLGtJg0p1YId48bY8Gtu40RuiGG0RlwmdXZrLo2qpNKAZfVErxOnIx4dsXYPbQlNOS5FKtQ4HyKjlHHjR01qn48fb8zAsDSBNk4mg5FjPtZqLCQ39rKk9Y9J0x4HkHtA3iXUqJKuLnE9YyR06CorDivcy4g-9nXdjcCCzf-EZfj8b_b7LNyLvAnV5mBf2s9GF_VjPbkVXtVOumLZcm5ev0Cr64Yo2R6fOY2ImvrcNFzF4oPJRQv_1vXkRk0AKtm8DD5NPQaWcTJyxA; '
        # 'cookiesu=391712910666794; '
        # 'u=391712910666794; '
        # 'device_id=b9e5b7077dc2f4f3faa2350feb34fd95; '
        # 'Hm_lvt_1db88642e346389874251b5a1eded6e3=1712910668; '
        # 'Hm_lpvt_1db88642e346389874251b5a1eded6e3=1712910668; '
        # 'smidV2=202404121631088e62844a41421f1a3c64d6af642bdc1900092a76ac7552300; '
        # '.thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=CTpcBbbrx+1XsC+sYt7kmwH4+L8kR1fyGeIPfGAo0gE16JhYQSFo+3nM0lPy0KUYtl4Hl3eEoTmLQkblDOjImg%3D%3D; '
        # 'acw_tc=276077b717129108189916378e071b39d059333fa8fcf44d24362e6b7b959d'
    ,
    'Referer': 'https://xueqiu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
