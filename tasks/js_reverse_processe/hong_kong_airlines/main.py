# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Project  : will-be-famous
@Time     : 2024/4/12
@Author   : Zhang ZiXu
@Software : PyCharm
@Desc     : 香港航空的 OB 混淆
@Last Modify          @Version        @Author
---------------       --------        -----------
2024/4/12               1.0             Zhang ZiXu
"""

import requests

url = "https://www.hongkongairlines.com/api/content/render/false/type/json/query/+contentType:HomepageHotcity%20+deleted:false%20+live:true%20+languageId:102/limit/0?timestamp__2482=CqGxBD9DgAGQeGKDseoYIh6EjF0QFiDcYtCoD"

payload = {}
headers = {
    'cookie': 'acw_tc=74d3dc1617129113109931358e2c20c63c6eb955ad503a733ffc334698; JSESSIONID=95eYqBrSGIC1XNVXsO8ab6lZ.HXDOTCMSServer5; opvc=1d8a9e32-895a-4184-bf83-776481af82f7; sitevisitscookie=1; dmid=2afe02e8-7250-4539-88f5-4a18e93b866f; BIGipServerpool_122.119.4.210_80=2702604154.20480.0000; ssxmod_itna=QqUx0D9DnDRGitoGH3iQR3ERzcSAb2GxAKoKQD/fQxnqD=GFDK40oE7PDCQt5o=Awi3Gqtr4hha3jmfeoKEFGYaUiadplmeDHxY=DU=DaPebDeW=D5xGoDPxDeDADYo0DAqiOD7qDd06TXZmqDEDYPDxitXD7U4reDjRqtcbeG0DDUHl4G27CtqDDNqYcGuYBQqieD+l32lBlUxFcqBD0tKxBdbRcDB0WHz=BXavcqqTr=DzTODtkXo6wTDCOUDgu0TW0oPmA5Knr4bFxe1zimxFDqPiG51i0x4lhmtf0GR4V+zn5DAn5qxD; ssxmod_itna2=QqUx0D9DnDRGitoGH3iQR3ERzcSAb2GxAKoKG9i5KDBqODD5GaW+IOrxKuAP7=D+OiD=',
    'referer': 'https://www.hongkongairlines.com/zh_CN/hx/homepage?telassa-id=IbeNotLogin~8C248FC65E4F13B0913CC7530BC287EA~hx-dev-PRD-0a05d86d-475739-12495&_catRootMessageId=hx-dev-PRD-0a05d86d-475739-12495&_catParentMessageId=hx-dev-PRD-0a05d86d-475739-12495&_catChildMessageId=hx-dev-PRD-0a05d86d-475739-12497&timestamp__2482=Gu0QiI4fEKBKDsD7GG7CcqYv86nNtCeD&alichlgref=https%3A%2F%2Fwww.hongkongairlines.com%2Fzh_CN%2Fhx%2Fhomepage%3Ftelassa-id%3DIbeNotLogin%257E8C248FC65E4F13B0913CC7530BC287EA%257Ehx-dev-PRD-0a05d86d-475739-12495%26_catRootMessageId%3Dhx-dev-PRD-0a05d86d-475739-12495%26_catParentMessageId%3Dhx-dev-PRD-0a05d86d-475739-12495%26_catChildMessageId%3Dhx-dev-PRD-0a05d86d-475739-12497',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
