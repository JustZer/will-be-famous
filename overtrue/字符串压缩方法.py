# -*- coding: utf-8 -*-
# @Time : 2022/7/8 14:00
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:
import base64
import gzip
import sys
import zlib


class StringFeildDensity:
    """
    gzip + base64 : gzip 底层就是 zlib
    glib + base64 : 压缩长字段可行,对于短字段起反效果。
    """
    def __init__(self):
        pass

    @staticmethod
    def gzip_zip_base64(content):
        """
        Gzip 压缩方法
        字节比 1000(压缩前) : 263.78(压缩后)
        Gzip + Base64 压缩方法
        字节比大约在 1000(源字符串字节) : 353.46(压缩后所占字节)
        Args:
            content: 传入的文本

        Returns:
            Gzip > Bytes
            Gzip + Base64 > String
        """
        print("## 正在使用 Gzip+base64 压缩方法")
        bytes_com = gzip.compress(str(content).encode("utf-8"))
        base64_data = base64.b64encode(bytes_com)
        back_content = str(base64_data.decode())
        print(f"## 源字符串所占字节大小: {sys.getsizeof(content)}, "
              f"压缩后 Gzip 所占字节大小: {sys.getsizeof(bytes_com)}, "
              f"压缩后 Gzip + Base64 所占字节大小: {sys.getsizeof(back_content)}")
        return back_content

    @staticmethod
    def gzip_unzip_base64(content):
        """
        Gzip + Base64 解压方法
        Args:
            content: 传入的文本

        Returns:
            String
        """
        base64_data = base64.b64decode(content)
        bytes_decom = gzip.decompress(base64_data)
        back_content = bytes_decom.decode()
        return back_content

    @staticmethod
    def zlib_zip(content):
        """
        Zlib 压缩方法
        字节比 1000(压缩前) : 261.27(压缩后)
        Zlib + Base64 压缩方法
        字节比 1000(压缩前) : 349.81(压缩后)
        Args:
            content: 传入的文本

        Returns:
            Zlib > Bytes
            Zlib + Base64 > String
        """
        print("## 正在使用 Zlib + Base64 压缩方法")
        bytes_com = zlib.compress(str(content).encode("utf-8"))
        base64_data = base64.b64encode(bytes_com)
        back_content = str(base64_data.decode())
        print(f"## 源字符串所占字节大小: {sys.getsizeof(content)}, "
              f"Zlib 压缩后所占字节大小: {sys.getsizeof(bytes_com)}, "
              f"压缩后 Zlib + Base64 所占字节大小: {sys.getsizeof(back_content)}")
        return back_content

    @staticmethod
    def zlib_unzip_zip(content):
        """
        Zlib 解压方法
        Args:
            content: 传入的文本

        Returns:
            String
        """
        base64_data = base64.b64decode(content)
        bytes_decom = zlib.decompress(base64_data)
        back_content = bytes_decom.decode()
        return back_content


if __name__ == '__main__':
    test_text = """<meta charset=\"utf-8\">\n<div>\n<meta charset=\"utf-8\"> <span></span>\n</div>\n<h4 style=\"text-align: center;"""
    Sfd = StringFeildDensity()
    a = Sfd.zlib_zip(test_text)
    print(f"压缩后文本: {a} \n { '=' * 33} \n ")
    print(f"压缩后数据类型为: {type(a)}")
    print(Sfd.zlib_unzip_zip(a))
