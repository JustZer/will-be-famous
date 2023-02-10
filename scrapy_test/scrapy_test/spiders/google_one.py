import time

import scrapy


class GoogleOneSpider(scrapy.Spider):
    name = 'google_one'

    # allowed_domains = ['google.com']
    # start_urls = ['http://google.com']

    def start_requests(self):
        meta = {
            "proxy": "https://127.0.0.1:10809"
        }
        cookies = {
            "ali_apache_id": "33.1.214.77.1673426776238.198445.8",
            "xman_t": "b+5SY3uN7q9jTcfW95f5q4TeH13UwFgQXTjiL8mMEf8i5CdGNkGGzj2YYDkUSYIp",
            "_ga_save": "yes",
            "ali_apache_track": "",
            "e_id": "pt100",
            "cna": "3dDgG0KyCzgCAW+sBs/0ktWe",
            "_fbp": "fb.1.1673426885349.1650577152",
            "_gcl_au": "1.1.1046802884.1673426885",
            "_ym_uid": "1673426886748929099",
            "_ym_d": "1673426886",
            "aep_usuc_f": "site=glo&c_tp=USD&region=HK&b_locale=en_US",
            "xman_f": "zbGLayMs2mpA2ZEFFS6iZ4dmdFT3YWQRfYkPlFNIe+F7RvusLYHo/uizIH13iXV6nH83MlCFDqjyu+7sljz/vLERpzopDUjtdKXteKDYQzbX4dYSu97MbQ==",
            "xlly_s": "1",
            "XSRF-TOKEN": "016bb4ce-4ec4-4781-93dc-d520398aa224",
            "intl_locale": "en_US",
            "acs_usuc_t": "x_csrf=pk_ca4umrqa0&acs_rt=eced7c713fa143c881b6891e55de0701",
            "_m_h5_tk": "19a97bb894b0e81b3b497c2bc37fa14a_1674009331079",
            "_m_h5_tk_enc": "92161686869236880fa086e1a1cf51f2",
            "_gid": "GA1.2.36609253.1674006723",
            "_ym_isad": "2",
            "xman_us_f": "x_locale=en_US&x_l=0&x_c_chg=0&x_as_i=%7B%22aeuCID%22%3A%22%22%2C%22cookieCacheEffectTime%22%3A1673427180728%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=6689399c81474c1e8e594f4d6f9bc81c",
            "_ga": "GA1.1.6a6f7395-924f-4a0d-bd50-c25246092e85.1673426855260",
            "cto_bundle": "L3Huel9TVHNOd2pjJTJCZGVUUkFrU2FRTk5YUU9Ya2xvWjloM2JxaUMwMGUxWms3eDN3MldBSFE5Y3RpN1FVd1Fwc2NSd0I3Nk9LVk1jTjVHREh0Q2tyd1F2NzIlMkJBeGJHbXVEakVDeGNKa3FJZm0lMkZDUFIyREF0RXBnYUplRlp4Ync3dllhdUpES0lBd2xUcDd4Vzc1d081aWhsRnclM0QlM0Q",
            "aep_history": "keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005003653446956%091005005065170979%0932829394958%0932815719981%091005005058037171%091005005058046562%091005005058400604%091005002172052150",
            "JSESSIONID": "A1592F6F492FF2B3C31E82315BEC2233",
            "intl_common_forever": "3kcs+8hiM4xv1FX7vleGN1JQxp0aQJYqUE2FLZrMHFaJZJeFYPCiFg==",
            "_ga_VED1YSGNC7": "GS1.1.1674023062.31.0.1674023063.0.0.0",
            "isg": "BKys_Yjq47iSbvbPOF0O8qngfYreZVAPPlfOsgboR9f6EU0bLnEJnv7oMdmpmYhn",
            "l": "fBEzpeDmLmOBXLl-BO5Churza77OWCdb8sPzaNbMiIEGa6wdsFgSzOCeZ8Dw-dtjgT52jetrhWAQudeyPVz38jkDBeYIKTiYwvvD8ews_gLN.",
            "tfstk": "cmzABpiwwTXcnsBizqIk7DW9YdZOCWXtFIMMWy_P0Um5MFwUCz1mqy4dkHIj1vkAw",
            "RT": "\"z=1&dm=aliexpress.com&si=2ed790d8-ad1b-4bc3-9281-edc63c412e76&ss=ld10do9k&sl=0&tt=0&bcn=%2F%2F684d0d48.akstat.io%2F&rl=1&ul=9qfa3\""
        }
        headers = self.get_headers()
        for product_id in ["1005003662001631", "1005004522340155", "1005003430572017"]:
            yield scrapy.Request(
                url="https://www.aliexpress.com/item/{}.html".format(product_id),
                method="GET",
                meta=meta,
                headers=headers,
                callback=self.parse,
                dont_filter=True,
                cookies=None
            )

    def parse(self, response):
        print(f"# 商品状态码为: {response.status} 链接: {response.url}")
        pass

    def get_headers(self, type='aliexpress'):
        if type == 'aliexpress':
            AliexpressHeaders = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                          "application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "max-age=0",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/81.0.4044.138 Safari/537.36 ",
            }
            cookie_dic = {
                '3': 'ali_apache_id=33.1.214.77.1673426776238.198445.8; XSRF-TOKEN=fa09c056-1905-4ed9-bf8a-f2ae1d64f3ef; intl_locale=en_US; xman_f=lIDxnbKXml3F1Q6ojny6Rf9+By1mXjxbHyji+JQ6lHxXijcNth4HnBmMQNPvLdcy6dIs66alHzCIcZ4g5ARObAnGHPPyjrjVGMNiAqDkFlZnDsCdcm+Kyg==; acs_usuc_t=x_csrf=pk_ca4umrqa0&acs_rt=6689399c81474c1e8e594f4d6f9bc81c; xman_t=b+5SY3uN7q9jTcfW95f5q4TeH13UwFgQXTjiL8mMEf8i5CdGNkGGzj2YYDkUSYIp; AKA_A2=A; _ga_save=yes; ali_apache_track=; ali_apache_tracktmp=; e_id=pt100; _m_h5_tk=a212cdf743fa84240f80f90b80cb6d7f_1673429492269; _m_h5_tk_enc=a6dfe2a68362a8441464e8521476a1cc; xlly_s=1; cna=3dDgG0KyCzgCAW+sBs/0ktWe; _gid=GA1.2.228555743.1673426885; _fbp=fb.1.1673426885349.1650577152; _gcl_au=1.1.1046802884.1673426885; _ym_uid=1673426886748929099; _ym_d=1673426886; _ym_isad=2; _ym_visorc=b; _gat=1; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005004610082890%091005004570308318; aep_usuc_f=site=glo&c_tp=USD&region=HK&b_locale=en_US; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&x_as_i=%7B%22aeuCID%22%3A%22%22%2C%22cookieCacheEffectTime%22%3A1673427180728%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=6689399c81474c1e8e594f4d6f9bc81c; JSESSIONID=DD93767EC29560B14BE8C76A1866EB17; intl_common_forever=bjxgm5iuYEGtKZcsySF53tNhNRVcPucMV2oBgauDvM7DJGm48+QQTg==; _ga_VED1YSGNC7=GS1.1.1673426394.23.1.1673428144.0.0.0; _ga=GA1.1.6a6f7395-924f-4a0d-bd50-c25246092e85.1673426855260; cto_bundle=FH9D319ET09WVWJjM1I3a1NHQ2tXN0hqU3ZZczRzQTBvcSUyQlpZbkE1cERSYUtkTWE1TEdPZkd5RjM5WFI4SE9xZTI5VnBqVG1qcCUyQk03VyUyRlpwRGxFT2ZCa1VpWW5TYmEzOHlNQnRVdG5YQVdFbHViR1BZUXZYUUlUaUZ6VnQxSFdhZ0EzSVdIR2d4VGFHWkdsYmdQSGx4VlJ3Z3clM0QlM0Q; tfstk=cpF1B2gcdhx6ep1Dsc_F7_tNj2lVZvLSlOig5GEYr7lRQya1ixOrVOX_nnhqk21..; l=fBEzpeDmLmOBXjFDBOfZourza779AIRAguPzaNbMi9fP_vfH5Y1AB67eg4YMCnGVF686R3kbtBa2BeYBqIYGkkwbdiL5Y6Mmn_vWSGf..; isg=BDQ0Zwsr69k2m34n8AUWmvHIBfKmDVj39m9GWs6V579COdSD9h8lhvH7vXHhwZBP; RT="z=1&dm=aliexpress.com&si=2ed790d8-ad1b-4bc3-9281-edc63c412e76&ss=lcreuk4k&sl=a&tt=tkm&obo=6&rl=1&ld=12j21&r=qidor4xj&ul=12j22"',
                '1': 'ali_apache_id=33.1.214.77.1673426776238.198445.8; XSRF-TOKEN=fa09c056-1905-4ed9-bf8a-f2ae1d64f3ef; intl_locale=en_US; xman_f=lIDxnbKXml3F1Q6ojny6Rf9+By1mXjxbHyji+JQ6lHxXijcNth4HnBmMQNPvLdcy6dIs66alHzCIcZ4g5ARObAnGHPPyjrjVGMNiAqDkFlZnDsCdcm+Kyg==; acs_usuc_t=x_csrf=pk_ca4umrqa0&acs_rt=6689399c81474c1e8e594f4d6f9bc81c; xman_t=b+5SY3uN7q9jTcfW95f5q4TeH13UwFgQXTjiL8mMEf8i5CdGNkGGzj2YYDkUSYIp; AKA_A2=A; _ga_save=yes; ali_apache_track=; ali_apache_tracktmp=; e_id=pt100; aep_usuc_f=site=glo&c_tp=HKD&region=HK&b_locale=en_US; _m_h5_tk=a212cdf743fa84240f80f90b80cb6d7f_1673429492269; _m_h5_tk_enc=a6dfe2a68362a8441464e8521476a1cc; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&x_as_i=%7B%22aeuCID%22%3A%22%22%2C%22cookieCacheEffectTime%22%3A1673427180728%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=6689399c81474c1e8e594f4d6f9bc81c; xlly_s=1; cna=3dDgG0KyCzgCAW+sBs/0ktWe; _gid=GA1.2.228555743.1673426885; _fbp=fb.1.1673426885349.1650577152; _gcl_au=1.1.1046802884.1673426885; _gat=1; _ym_uid=1673426886748929099; _ym_d=1673426886; _ym_isad=2; _ym_visorc=b; _ga_VED1YSGNC7=GS1.1.1673426394.23.1.1673426895.0.0.0; _ga=GA1.1.6a6f7395-924f-4a0d-bd50-c25246092e85.1673426855260; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005004610082890; l=fBEzpeDmLmOBXuTbBOfwPurza77OSIRAguPzaNbMi9fPOhCp5FzFB67e1S89C3GVFsCMR3kbtBa2BeYBqn0o9kPSZnZJSFDmn_vWSGf..; tfstk=cVLfBAfiV-2jMD3gotGrg21cnjb1ZzNC1m6DGxp9pUu_c9OfiOaFdmmXjRQN6_1..; isg=BDEx7XN19n7IjVtYDXb7nYQLQL3LHqWQI8zjxRNGLfgXOlGMW261YN9YWM5c8j3I; cto_bundle=bdgVHV9xODFuJTJCWktkRVluRHNIOGxqdFp4UnRZck9za2JhVlFBczh1dVY2WWtsV1FicmxwQ3Z2Yk5ldDklMkZYTUtZaUpvR1N1WDFhenp1emRSbjdNMGNQb1lXNm5UVndmWDB2b3QzY2VPQlREY2ZiOTg3a2FmJTJGZzd5dDFFaldwN01KaTY4Rjk1d1pUU3o2UDdKdzkxQ2Q5VjIwV1ElM0QlM0Q; JSESSIONID=93F264F3C6F4B4E01A8729296771D103; intl_common_forever=/S99GrZuV0tpnr1TkgM53YXcf2+sBlbL/ajQL9qP3FYIP1UdqvoVmw==; RT="z=1&dm=aliexpress.com&si=2ed790d8-ad1b-4bc3-9281-edc63c412e76&ss=lcreuk4k&sl=6&tt=cbf&obo=5&rl=1&ld=bl7i&r=chz0ojpue&ul=bl7j"',
                '2': 'ali_apache_id=33.54.47.26.1667789573323.193410.0; xman_t=PvNQt9Lhw+YPZ1bRrdKbKUaS8NWpEalpFOrnLTSzs+6ton5v8iT3cxo4q0HSx0T0; cna=3dDgG0KyCzgCAW+sBs/0ktWe; _gcl_au=1.1.77996736.1667789577; _ym_uid=1662690410108174045; _ym_d=1667789579; ali_apache_track=; _bl_uid=d9ljUa9w6pg646uXzy7zxpFly5hw; _fbp=fb.1.1669623249604.1560875797; e_id=pt80; account_v=1; xman_f=jHqMmvh/f6v2VHcquOe3KLH4LM8sakGOA6wbhfcxmhlA4uSVRs7Qkzdu/A4eBTC1CBZFUN2Mbm+aL8kS2MRSyrEdZL/9NS2gKCkYQIewMd7+5fUMC1GlwQ==; xlly_s=1; intl_locale=en_US; AKA_A2=A; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1670554974839%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=1566a9cf8725409ca0a265ca12cc7e6b; acs_usuc_t=x_csrf=k4sdl4dl2pjr&acs_rt=80bd6c1ebbb74a618b82f32395e91716; _m_h5_tk=eb275b4992b68d251117eae69cd27432_1673428892608; _m_h5_tk_enc=6fc07d7ac8cbe636c31b9325e01e7450; _gid=GA1.2.730309183.1673426376; XSRF-TOKEN=69a9aec6-06c3-4266-9a77-2c364ea305ba; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005003970178494%0933009545505%091005002949808991%091005002003179693%091005004800259609%091005003853011498%094000956069019%091005004174696596; _ym_isad=2; _ym_visorc=b; JSESSIONID=9B5941B6F8A8DA6636696B502B37BC65; intl_common_forever=hSccpu4jyTj5gK2Jx4i9jzn9ZuTC0xbJ2YPgEphYqFdM7n1rKcHB8Q==; _ga_VED1YSGNC7=GS1.1.1673426394.23.1.1673426411.0.0.0; _ga=GA1.1.120438868.1667789577; cto_bundle=UpUeN19KSjFPTnZOd3pqSHBzcHViNUlDJTJGOEVGbXZXR3FaSE5uQmFlQ1o1UTNMJTJGa0dhcVZ3JTJCZXYyWTE2SDZTN2RRZ05hbjRPSXVSTFg1Z29naDFENTlHOCUyRkdEYVYlMkJJT1NLSzR2UDRZSyUyQlRxdkdVcTlPTVVOVGNwV3BaJTJGUksxcjhsbHpnSlBCQmg0VWVUeW1RNnM2MmQxQk1ldyUzRCUzRA; tfstk=cdDFBOcy_ppeMBiJkR2r_F7j_85dZeonqOrbtU7Aavzhv4Fhip_8jWU0busNrWf..; l=fBEzpeDmLmOBX-2oBOfZourza779JIRAguPzaNbMi9fP_85M5LKFB67esyLHCnGVF6y6R3kbtBa2BeYBqGXckkwj4XpHTFkmn_vWSGf..; isg=BL6-zQapUdcxwoTBFrc8xC-aD9QA_4J5eJ2cPGjHHoH8C17l0IyTikShg9fHM3qR; RT="z=1&dm=aliexpress.com&si=2ed790d8-ad1b-4bc3-9281-edc63c412e76&ss=lcreuk4k&sl=3&tt=cbf&obo=2&rl=1&ld=7sta&r=7v8dbp112&ul=7stb"',
                '0': 'ali_apache_id=33.54.47.26.1667789573323.193410.0; xman_t=PvNQt9Lhw+YPZ1bRrdKbKUaS8NWpEalpFOrnLTSzs+6ton5v8iT3cxo4q0HSx0T0; cna=3dDgG0KyCzgCAW+sBs/0ktWe; _gcl_au=1.1.77996736.1667789577; _ym_uid=1662690410108174045; _ym_d=1667789579; ali_apache_track=; _bl_uid=d9ljUa9w6pg646uXzy7zxpFly5hw; _fbp=fb.1.1669623249604.1560875797; e_id=pt80; account_v=1; xman_f=jHqMmvh/f6v2VHcquOe3KLH4LM8sakGOA6wbhfcxmhlA4uSVRs7Qkzdu/A4eBTC1CBZFUN2Mbm+aL8kS2MRSyrEdZL/9NS2gKCkYQIewMd7+5fUMC1GlwQ==; xlly_s=1; intl_locale=en_US; AKA_A2=A; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1670554974839%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=1566a9cf8725409ca0a265ca12cc7e6b; acs_usuc_t=x_csrf=k4sdl4dl2pjr&acs_rt=80bd6c1ebbb74a618b82f32395e91716; _m_h5_tk=eb275b4992b68d251117eae69cd27432_1673428892608; _m_h5_tk_enc=6fc07d7ac8cbe636c31b9325e01e7450; _gid=GA1.2.730309183.1673426376; XSRF-TOKEN=69a9aec6-06c3-4266-9a77-2c364ea305ba; _gat=1; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005003970178494%0933009545505%091005002949808991%091005002003179693%091005004800259609%091005003853011498%094000956069019%091005004174696596; cto_bundle=XLrlcF9VdUhXdmF6Y0FDYmNkdzV6a2ljRnpvemprVzBlT3MwUmFZeHc3ZmhGM2x5WUFaNmJ1RGw5NTZJUGVuRmFQWVREcGFyRHBQa2g3bVpCd29MZkczM3glMkJubmpnOUc2VDJNSXBZeFV5WDZWUngzQ3oxSFBmUEVCalo2Tk9BWHlZTk0lMkJ1MHRzSXJnZk1GdFVKTExJb0VCelJBJTNEJTNE; _ga=GA1.1.120438868.1667789577; _ga_VED1YSGNC7=GS1.1.1673426394.23.1.1673426394.0.0.0; tfstk=cv1hBkvOw9JQSbPRfMOQMRNxAMeOZxhym_51_PPxLh1AdtCNipMZ3FLgSHqbYY1..; isg=BGVlUToDatqm3I80WXr3-RjPdCGfohk0DwhX6WdKKByrfoXwL_CGBf4cDOII_jHs; l=fBEzpeDmLmOBXWGoBOfwPurza77tjIRAguPzaNbMi9fP_kfp5O25B67es8Y9CnGVFsGWR3kbtBa2BeYBqn0o9kPS4XpHTCMmn_vWSGf..; _ym_isad=2; _ym_visorc=b; JSESSIONID=056C648C4A13CE814DBD614E0500562C; intl_common_forever=2NPixBfzd1JPACxXau7lGCGy6+pF1q6DovsmxjVLT+QtEjSc/P8vCA==; RT="z=1&dm=aliexpress.com&si=2ed790d8-ad1b-4bc3-9281-edc63c412e76&ss=lcreuk4k&sl=2&tt=cbf&rl=1&obo=1&ld=uy8&r=7v8dbp112&ul=uy9"'
            }
            key = time.strftime('%H')
            if int(key) < 8:
                AliexpressHeaders['cookie'] = cookie_dic['0']
            elif int(key) < 16:
                AliexpressHeaders['cookie'] = cookie_dic['1']
            else:
                AliexpressHeaders['cookie'] = cookie_dic['2']
            AliexpressHeaders['cookie'] = cookie_dic['3']
            return AliexpressHeaders
