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
import re

import execjs
import requests

headers = {
    "Accept": "*/*",
    "Referer": "https://xueqiu.com/today",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
}
url = "https://xueqiu.com/today"
data = {
    "-1|1713270595652|windows|2560x1441|1043|1000|1|{\"cookiesu\":\"801713270595127\",\"ua\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0\",\"referurl\":\"https://xueqiu.com/today\",\"url\":\"https://xueqiu.com/today\",\"tab\":\"全球\",\"sub_tab\":\"1小时内最热\"}-1|1713270595700|windows|2560x1441|111|1000|1|{\"cookiesu\":\"801713270595127\",\"ua\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0\",\"referurl\":\"https://xueqiu.com/today\",\"url\":\"https://xueqiu.com/today\",\"source\":503,\"trigger\":\"push\"}-1|1713270596170|windows|2560x1441|1050|1000|1|{\"cookiesu\":\"801713270595127\",\"ua\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0\",\"referurl\":\"https://xueqiu.com/today\",\"url\":\"https://xueqiu.com/today\"}-1|1713270596172|windows|2560x1441|0|503|1|{\"cookiesu\":\"801713270595127\",\"ua\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0\",\"referurl\":\"https://xueqiu.com/today\",\"url\":\"https://xueqiu.com/today\"}{\"appId\":\"xqweb\",\"organization\":\"4mj8mWhcvi7MJ5sa3oqG\",\"ep\":\"M611qNJZgeuP5pThZcqWhPoq3n904fZvW1T1S2izp9z3iRpUmkJLbCWRqsdFjw/n19s/XULOCjAUCpjDa0x2f34Xpz1rXabF+5UwhpFu9CRerKRNaNhsXOc3nSz6eveY8/tcthOkOsJ6UdLfCgpCeOaC3xQ8z6eM+jQhVX/PszI": "\",\"data\":\"50837ca832c0c654538b1b74066a43db9dd6e88ce81805bb23c2e0caeaf8d49f68f4124237f44e74bff5388d1ed11eee7a88ee4357e93f9859143023ca6ac22653b55327c1b0421a907380bc55a36dfa9bea70c34b7d01ce14a450b763e75d32cc42d43ec896b7a294491b4be5b62fca4d0e0a10c5ec183da39ff1a14106df3d53d771473e265b573996312a40e500b9c08aee0a270a67ee7a0ba0a0042e24c63a31d2cbf8552a4e7138f3f8fcd0219fbdfe156e84f971c045ea1159afca8950f90a1b3e01b3a55a44480f640df557a247761c2a35231be9a14a4ee8945e007dc54920e28af54fee5b03bd7d0d02191c51652602229f85f6bea5b7e74818a3b31f486db66c637204461e7e7ecd6519c6cbbce2a693e88deb8e1123d39cf13a4ae062b6e4a4e172c6e877bed972a07beac383b4af2252fd855dd9f6a2c5e5ee162235a5ae7b780461b87c19b28dd68c15a7ebac4602651e1a1096c18a66a8115b27d7bdb02730a3fbe649e37c1ec889c2f772dcd1e2412060fe48faf9efed4d3adb417722c1ddfd7bf2b95336ee6f0d4471da9b7cc60d129c572c7c4a18c2c9696dd73605cf5ec04e9cf3e5226979c187841411c67513375b5d28e4bf13d8afbb063fa8668e020ad3cb2f9f181e77180049e817a9763c8215a7d90ab3878771b8f84932cb4f24d9703e656cb6d9d0be9ce836353db11ae04d236975906ad6ffd6835473c8e921b5359134fe128861b9c8cf94eeec73d61289d52889533ea3e360f558c3a1d43e9486c9144ef817146757246d5ce1dfd98af3484b1d0a4d724c523d550eac939f05d8135c6d07568a045b7dec031a00aae75021023f7f04af98de4a2843f7da67ec1521d60734a6afce273d5ebda4c42bd7d0a29c03c27710361399a2d45230e10d346e4e1629966a6d67f1afcc0853cebaa65aa6980ce7300e8da21f7e951008d52a38deebc17e9d6540075edda4516fe9c5391cea3c470669bcd4fe0b95e42c3a6a64774ae89bade9f7f0be07a4b9728f48db74105167657e70222e3da6efdf78c9c70d7ac386a830088dbbbdd376909d9bd91c35ec30989cad88424a152df1173f2f5c11d25ad867937d9824c0c542a09b1d97f50b18979ac4f978ade5fa3fcd5bd4dd10ddff6e8b14570e4e7c9a6f9a91838b1db7b0e972b55cd91371c88a15c41bf10844bad315ecc26d2d6b982b2370bea0dd6649822e05b527727e9674f28c4c784e36bd025c3fd053cf928b5b3638ce4d2350d3bb29cbcea2fe1e782139a97466df58a22e946020d4c2d24fd0e10004f2635af5e976880434cff788dfbe2a2964e3cdbb16ad5693c4e87849d290aaa3e5e156c6b38f01a2c1ff3eb519fa613687c7ef338a86685e2daa722838dceaaaafa3e6e54314d4947bd2071bd7cbf0885697370f52677dd0c4dfce8ad1b242cb15b166fb7a120ccc13e74f6e7d2adef40d7e92f481660fca003ee43c3d075a879868de43c45b9b9bd850982eef0b71c2bc7aca2c3f6fa90053d04a1d4536be7dc6c09eacbb26bdb9be4f7b9e94f63a6ded4a668087538b1ae37c89724ac6fb52e9e7c7c7d4830aae45717e128635974a1c60395656a8c0939854ea02557f3d60c65c77832627b85eb86d52c15f51565f7855a3ed51f33dd2a64e523e508708ecae53e4be6b18a29fb61fc567ddaa455cc9a3c59fedc3fe745c4166d6364f08fd73a213d28f8d32c4cae2bba74b6937f0c9b7d5bc013d7ec27793d38a1773f1e0d8b212d855cf2dc06b5d72763f3b5f6fd17efc8b423efd18e0d7ce037bf16c9a2ed766eeb0c6e58fc1cc6a46cb4141a1eb42a0f29f4781d6da2929410c4d20168ae51e3f2b2a36d0243b5983aea321c366a868d98126f53a53b5781540b41adaae00bde140f817d749b572baa01968baccfd7c0c783f94f58bfaa995bf2f1fd0d792c037970c0e346d93a4a4d9e6e36f86d6eefcfca820\",\"os\":\"web\",\"encode\":5,\"compress\":2}${\"metadata\":{\"service\":{\"name\":\"snowman-web\",\"agent\":{\"name\":\"js-base\",\"version\":\"4.1.2\"},\"language\":{\"name\":\"javascript\"}}}}\n{\"transaction\":{\"id\":\"ad0f689ac6434814\",\"trace_id\":\"8d9408d93f8037caedb42f90cff65fac\",\"name\":\"other pages\",\"type\":\"page-load\",\"duration\":1660.2999999523163,\"context\":{\"page\":{\"referer\":\"https://xueqiu.com/today\",\"url\":\"https://xueqiu.com/today\"}},\"marks\":{\"navigationTiming\":{\"fetchStart\":0,\"domainLookupStart\":2,\"domainLookupEnd\":2,\"connectStart\":2,\"connectEnd\":64,\"secureConnectionStart\":31,\"requestStart\":64,\"responseStart\":108,\"responseEnd\":108,\"domLoading\":111,\"domInteractive\":714,\"domContentLoadedEventStart\":714,\"domContentLoadedEventEnd\":714,\"domComplete\":1455,\"loadEventStart\":1455,\"loadEventEnd\":1456},\"agent\":{\"timeToFirstByte\":108,\"domInteractive\":714,\"domComplete\":1455,\"firstContentfulPaint\":379}},\"span_count\":{\"started\":0},\"sampled\":false}}\n"
}
response = requests.options(url, headers=headers, data=data)

cookie = response.cookies.get_dict()

# with open('xu_qiu_01.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)

response_text = re.sub("\s", "", response.text)
arg1 = re.findall("vararg1='(.*?)';", response_text)[0]

arg2 = execjs.compile(open("demo.js", "r", encoding="utf-8").read()).call("main123", arg1)
print(arg2)

cookie["acw_sc__v2"] = arg2

print(cookie)
