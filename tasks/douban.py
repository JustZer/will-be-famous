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
from urllib.parse import urlparse

import requests


def gen_rqsession(referer_url: str = '', origin_url: str = '') -> requests.Session:
    '''
    生成新的 Requests 会话
    :param referer: 请求来源
    :param origin: 请求源
    :return: 会话对象
    '''
    if referer_url and (not origin_url):
        o = urlparse(referer_url)
        origin_url = o.scheme + "://" + o.netloc
    sess = requests.Session()
    sess.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': referer_url,
        'Origin': origin_url
    })
    return sess


def c_douban_info(isbn: str) -> dict:
    '''
    从豆瓣获取图书评分
    :param isbn: ISBN 号
    :return: 图书评分字典
    '''
    data = {}
    try:
        referer_url = f'https://search.douban.com/book/subject_search?search_text={isbn}&cat=1001'
        with gen_rqsession(referer_url) as sess:
            url = f'https://book.douban.com/j/subject_suggest?q={isbn}'
            resp = sess.get(url, timeout=(3, 5))
            content = resp.json()[0]
            print(content)
    except Exception as e:
        print(e)


c_douban_info("9787557028589")
