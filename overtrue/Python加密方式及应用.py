# -*- coding: utf-8 -*-
# @Time : 2022/7/22 16:57
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:
import loguru


class PythonEncryptionMethod:
    def __init__(self):
        self.logger = loguru.logger

    def func_base64(self, string: str):
        """
        ey 开头是字符串 {" 开头的内容的 base64 ，解码后大概率是 JSON
        aHR0c 开头是 http 的 base64 ，解码后大概率是 URL 网址
        PE 、PF 、PG 、PH 开头的 base64 ，解码后有可能是 xml 或者 html 文本
        Args:
            string:

        Returns:

        """
        import base64
        b64_encode = base64.b64encode(string.encode())
        self.logger.info(f"base64 加密在之后的结果: {b64_encode}")
        # self.logger.info(base64.b64decode(string.encode()))


if __name__ == '__main__':
    pem = PythonEncryptionMethod()
    pem.func_base64("我是你爹,123123,[123,456,789]")
