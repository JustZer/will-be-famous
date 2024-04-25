# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Project  : webspiders
@Time     : 2024/4/24
@Author   : Zhang ZiXu
@Software : PyCharm
@Desc     : 企查查搜索爬虫
@Last Modify          @Version        @Author
---------------       --------        -----------
2024/4/24               1.0             Zhang ZiXu
"""
import copy
import hashlib
import hmac
import json
import logging
import re
import time

import requests

from common_tools.database_tools.db_model import PdcQccPublisherInfo, PdcQccPublisherDetail
from common_tools.utils.logger_manager import LoggerUtil
from common_tools.utils.re_utils import ReUtils


class QccSearchSpider:
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    }

    def __init__(self, _logger: logging.Logger, cookies=""):
        self.logger = _logger
        self.headers["cookie"] = cookies
        self.re_utils = ReUtils()

    def main(self):
        rows = PdcQccPublisherInfo.select().where(PdcQccPublisherInfo.id > 33)
        for row in rows:
            keyword = row.publisher_name
            self.logger.info(f"开始获取企查查信息: {keyword}")
            json_response = self.get_qcc_company_info(keyword)
            publisher_info = self.parser_publisher_info(json_response)

            # 数据库存储
            if publisher_info:
                self.logger.info(f"{keyword} > 数据获取成功")
                row.uscc_id = publisher_info["uscc_id"]
                row.incorporation_date = publisher_info["incorporation_date"]
                row.publisher_province = publisher_info["publisher_province"]
                row.legal_persons = publisher_info["legal_persons"]
                row.registered_capital = publisher_info["registered_capital"]
                row.publisher_address = publisher_info["publisher_address"]
                row.publisher_status = publisher_info["publisher_status"]
                row.save()
                self.logger.info(f"{keyword} > 数据【基本信息】存储成功")

                financial_info = publisher_info["financial_info"]
                if [bool(_) for _ in list(financial_info.values())].count(True):
                    new_financial_info = self._combine_financial_data(financial_info)
                    for year, data in new_financial_info.items():
                        defaults_dict = {}
                        if int(data.get("revenue_info", {}).get("revenue", 0)):
                            defaults_dict["revenue"] = int(data["revenue_info"]["revenue"])
                        if int(data.get("profit_info", {}).get("value", 0)):
                            defaults_dict["profit"] = int(data["profit_info"]["value"])
                        if int(data.get("total_assets_info", {}).get("value", 0)):
                            defaults_dict["total_assets"] = int(data["total_assets_info"]["value"])

                        detail_row, is_new = PdcQccPublisherDetail.get_or_create(
                            defaults=defaults_dict,
                            uscc_id=publisher_info["uscc_id"],
                            report_year=year,
                            publisher_person_num=publisher_info.get("publisher_people")
                        )
                        if is_new:
                            self.logger.info(f"{keyword} > {year} 财报数据 > 新增【数据详情】存储成功")
                        else:
                            for k, v in financial_info.items():
                                setattr(detail_row, k, v)
                            detail_row.save()
                            self.logger.info(f"{keyword}> {year} 财报数据 > 更新【数据详情】存储成功")
                else:
                    self.logger.info(f"{keyword} > 数据【数据详情】获取失败, financial_info 信息: {financial_info}")
            else:
                self.logger.info(f"{keyword} > 数据获取失败")

            time.sleep(7)

    def parser_publisher_info(self, json_response):
        info = {}
        try:
            if "Result" in json_response and json_response["Result"]:
                company_info = json_response["Result"][0]

                uscc_id = company_info["CreditCode"]
                # 获取公司成立日期
                incorporation_date = self._get_publisher_incorporation_date(json_response)
                # 获取公司省份
                publisher_province = company_info.get("Area", {}).get("Province")
                # 获取公司法人信息
                legal_persons = company_info["OperName"]
                # 获取注册资本
                registered_capital = company_info.get("RegistCapi", "").replace("万元人民币", "")
                # 获取公司地址
                publisher_address = self.re_utils.remove_html_label(company_info.get("Address", ""))
                # 获取公司注册状态
                publisher_status = company_info.get("Status", "").split("（")[0]
                # 获取公司人数
                publisher_people = self._get_publisher_people(company_info)
                # 获取公司营业收入
                financial_info = self._get_financial_info(company_info)

                info.update({
                    "uscc_id": uscc_id,
                    "incorporation_date": incorporation_date,
                    "legal_persons": legal_persons,
                    "publisher_province": publisher_province,
                    "registered_capital": registered_capital,
                    "publisher_address": publisher_address,
                    "publisher_status": publisher_status,
                    "publisher_people": publisher_people,
                    "financial_info": financial_info,
                })

        except Exception as e:
            self.logger.info(f"企查查获取信息失败: {e}")
        return info

    def get_qcc_company_info(self, keyword: str):
        url = 'https://www.qcc.com/api/search/searchMulti'
        data = {
            'searchKey': keyword,
            'pageIndex': 1,
            'pageSize': 1
        }
        pid, tid = self._get_pid_and_tid()

        # 构建请求头
        headers = copy.deepcopy(self.headers)
        headers["origin"] = "https://www.qcc.com"
        headers["referer"] = "https://www.qcc.com/web/search/advance?hasState=true"
        headers["x-requested-with"] = "XMLHttpRequest"
        headers["x-pid"] = pid
        # 构建加密链
        headers_key = self.a_default("/api/search/searchMulti", data)
        headers_value = self.r_default("/api/search/searchMulti", data, tid)
        headers[headers_key] = headers_value

        response = requests.post(url, headers=headers, json=data).json()

        return response

    def _get_pid_and_tid(self):
        """
        获取pid, tid
        Returns:

        """
        url = 'https://www.qcc.com/web/search/advance?hasState=true'

        headers = copy.deepcopy(self.headers)

        res = requests.get(url, headers=headers).text
        try:
            pid = re.findall("pid='(.*?)'", res)[0]
            tid = re.findall("tid='(.*?)'", res)[0]
        except Exception as e:
            self.logger.warning("## pid, tid 匹配失败, 请检查当前接口(web/search/advance)匹配逻辑是否发生变动.")
            pid = ''
            tid = ''

        return pid, tid

    def a_default(self, url: str = '/', data: object = {}):
        url = url.lower()
        data_json = json.dumps(data, ensure_ascii=False, separators=(',', ':')).lower()

        _hash = hmac.new(
            bytes(self._seeds_generator(url), encoding='utf-8'),
            bytes(url + data_json, encoding='utf-8'),
            hashlib.sha512
        ).hexdigest()
        return _hash.lower()[8:28]

    def r_default(self, url: str = '/', data: object = {}, tid: str = ''):
        url = url.lower()
        data_json = json.dumps(data, ensure_ascii=False, separators=(',', ':')).lower()

        payload = url + 'pathString' + data_json + tid
        key = self._seeds_generator(url)

        _hash = hmac.new(
            bytes(key, encoding='utf-8'),
            bytes(payload, encoding='utf-8'),
            hashlib.sha512
        ).hexdigest()
        return _hash.lower()

    @staticmethod
    def _seeds_generator(s):
        seeds = {
            "0": "W",
            "1": "l",
            "2": "k",
            "3": "B",
            "4": "Q",
            "5": "g",
            "6": "f",
            "7": "i",
            "8": "i",
            "9": "r",
            "10": "v",
            "11": "6",
            "12": "A",
            "13": "K",
            "14": "N",
            "15": "k",
            "16": "4",
            "17": "L",
            "18": "1",
            "19": "8"
        }
        seeds_n = 20

        if not s:
            s = "/"
        s = s.lower()
        s = s + s

        res = ''
        for i in s:
            res += seeds[str(ord(i) % seeds_n)]
        return res

    def _get_publisher_incorporation_date(self, company_info):
        if "GroupItems" in company_info and company_info["GroupItems"]:
            for item in company_info["GroupItems"]:
                if item["key"] == "startdateyear":
                    if "items" in item and item["items"]:
                        return item["items"][0]["value"]

    def _get_publisher_people(self, company_info):
        if "CountInfo" in company_info and company_info["CountInfo"]:
            for item in company_info["CountInfo"]:
                if item["k"] == "36":
                    value = json.loads(item["v"])
                    return value["c"]

    def _get_financial_info(self, company_info):
        """
        处理公司财务信息，包括总收入、净利润和总资产。

        Args:
            company_info (dict): 包含公司信息的字典。

        Returns:
            dict: 包含总收入、净利润和总资产信息的字典。
        """
        # 用于存储财务数据的字典
        financial_data = {
            "revenue_info": {},
            "profit_info": {},
            "total_assets_info": {}
        }

        # 键映射关系
        key_map = {
            "48": ("revenue_info", "Revenue", "RevenueYear"),
            "55": ("profit_info", "Value", "Year"),
            "53": ("total_assets_info", "Value", "Year")
        }

        # 解析公司信息
        if "CountInfo" in company_info and company_info["CountInfo"]:
            for item in company_info["CountInfo"]:
                key_data = key_map.get(item["k"])
                if key_data:
                    info_key, value_key, year_key = key_data
                    values = json.loads(item["v"])
                    for v in values:
                        year = v[year_key]
                        report_type = v["ReportType"]
                        value = v[value_key]
                        # 更新或设置信息
                        current_info = financial_data[info_key].setdefault(year, {})
                        if current_info.get("report_type", 0) < report_type:
                            current_info["report_type"] = report_type
                            current_info[value_key.lower()] = value

        return financial_data

    def _combine_financial_data(self, financial_data):
        """
        将不同财务信息按年度合并为一个字典。

        Args:
            financial_data (dict): 包含多个财务类别信息的字典。

        Returns:
            dict: 按年度组合的财务信息字典。
        """
        combined_data = {}
        for category, years_data in financial_data.items():
            for year, data in years_data.items():
                if year not in combined_data:
                    combined_data[year] = {}
                combined_data[year].update({category: data})
        return combined_data


if __name__ == '__main__':
    cookies = "QCCSESSID=9ddcfddd4c64194db5e3c34c93;UM_distinctid=18f036f95611f07-008929315c6c32-4c657b58-384a00-18f036f9562292a;acw_tc=3a31f99e17137545651434131e434f555f2e9b7e6c8e0d50b14285104e; tfstk=feSkuqmIha876QkLZix70HZ22HUYFbtB76np9HdUuIRjwbnRLHRhTIIJwTKrFZ1OQ0I8PHnHVHtU65ETXTBWAHok7OekNtWXLjQL1yB5FHMXE1W1OTgH62m1YH5e0nJWLHJyzeJ4nppBUHRy8ju2QIReYH5e0IJ6UboezDoV3bUirCIF7iy9yrTCoHWhmLY4kTRqGeSDEUANUgmEYVJkrCWyi5EQux8VdejIdDYdUN1BQ_lztBsc3g7N_S3JaNvhBwfap49v-gtDTgrsIISlKiY5kbuyI3Ak7g5qCRBD8ZjD2gPI5tBDaFxAkrNJJ3fl5CTzlS1hnQCFqEluMBQOHg8c_SncOebF2nSzgljPVquZ1TnB3JIqR2TyhKAsft5rFGYfPTw0nVBpzK966Mem-RcsY0OTn-0OYUJXCCC..;"
    _logger = LoggerUtil("qcc_search_spider", logger_level="DEBUG").get_logger()
    qcc_spider = QccSearchSpider(_logger=_logger, cookies=cookies)
    qcc_spider.main()
    # print(response)
