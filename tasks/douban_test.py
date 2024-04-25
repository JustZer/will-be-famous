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
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    # 'Connection': 'keep-alive',
    'Referer': 'https://search.douban.com/book/subject_search?search_text=9787557028589&cat=1001',
    'Origin': 'https://search.douban.com'

}
isbn = "9787557028589"
url = f'https://book.douban.com/j/subject_suggest?q={isbn}'

response = requests.get(url, headers=headers)

print(response.text)