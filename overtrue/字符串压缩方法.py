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
    def __init__(self):
        pass

    def gzip_zip_base64(self, content):
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

    def gzip_unzip_base64(self, content):
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

    def zlib_zip(self, content):
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

    def unzlib_zip(self, content):
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
    test_text = """<meta charset=\"utf-8\">\n<div>\n<meta charset=\"utf-8\"> <span></span>\n</div>\n<h4 style=\"text-align: center;\" data-mce-style=\"text-align: center;\">Addon en polymère \"Inima\" couleur à choix, de la collection \"Love\"<br><meta charset=\"utf-8\">\n</h4>\n<h4 style=\"text-align: center;\" data-mce-style=\"text-align: center;\">(photo non contractuelle, seul l'addon est compris dans la commande)</h4>\n<h4 style=\"text-align: center;\" data-mce-style=\"text-align: center;\">\n<br><br>Design : Amila Pousaz<br>\n</h4>\n<div style=\"text-align: center;\"><img src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/love5.web_1024x1024.jpg?v=1634294355\" width=\"1024x1024\" height=\"1024x1024\" style=\"float: none;\"></div>\n<div style=\"text-align: center;\"><img style=\"float: none;\" alt=\"\" src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/love7.web_1024x1024.jpg?v=1634294371\"></div>\n<h4 style=\"text-align: center;\" data-mce-style=\"text-align: center;\">\n<img alt=\"\" src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/love6.web_1024x1024.jpg?v=1634294402\" style=\"float: none;\"><img style=\"float: none;\" alt=\"\" src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/love8.web_1024x1024.jpg?v=1634294419\">\n</h4>\n<h1 style=\"text-align: center;\" data-mce-style=\"text-align: center;\">Précautions / informations<br>\n</h1>\n<div class=\"p1\">\n<div style=\"padding-left: 90px;\"></div>\n<p class=\"p1\" style=\"text-align: left; padding-left: 90px;\" data-mce-style=\"text-align: left; padding-left: 90px;\">Nous vous rendons attentifs au fait que la couleur de l'addon et de ses dessins peuvent varier selon la lumière.<br></p>\n<p class=\"p1\" style=\"padding-left: 90px;\" data-mce-fragment=\"1\"><meta charset=\"utf-8\"><span data-mce-fragment=\"1\">Attention, les addons en </span><span class=\"il\" data-mce-fragment=\"1\">polymère</span><span data-mce-fragment=\"1\"> sont sensibles aux produits chimiques, notamment au parfum, solvant, désinfectant pour les mains, acétone ou autre produit similaire ! </span><span data-mce-fragment=\"1\">Dans la réalité, nous nous efforçons, de nous approcher le plus possible de la couleur des addons figurant dans le shop. Cependant, il peut y avoir des légères différences de teinte.<br></span><strong data-mce-fragment=\"1\"> <br>Attention : cet addon n'est pas compatible avec la base extra small (9mm).</strong></p>\n<p class=\"p1\" style=\"text-align: left; padding-left: 90px;\" data-mce-style=\"text-align: left; padding-left: 90px;\"><br> </p>\n</div>\n<h1 style=\"text-align: center;\" data-mce-style=\"text-align: center;\">Notre inspiration<br>\n</h1>\n<div style=\"text-align: center;\">\n<img src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/INIMANOIR_480x480.png?v=1634288122\" width=\"600x600\" height=\"600x600\" style=\"float: none;\" data-mce-fragment=\"1\" data-mce-src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/INIMANOIR_480x480.png?v=1634288122\"><br> <br><img src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/INIMA_480x480.png?v=1634288133\" width=\"600x600\" height=\"600x600\" style=\"float: none;\" data-mce-fragment=\"1\" data-mce-src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/INIMA_480x480.png?v=1634288133\"><br> <br><img src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/image_e080419c-39c6-498f-8be0-24a71bfae4a4_480x480.png?v=1634225677\" width=\"600x600\" height=\"600x600\" style=\"float: none;\" data-mce-fragment=\"1\" data-mce-src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/image_e080419c-39c6-498f-8be0-24a71bfae4a4_480x480.png?v=1634225677\"><br> <br><img src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/love17.web_480x480.jpg?v=1634302667\" width=\"600x600\" height=\"600x600\" style=\"float: none;\" data-mce-fragment=\"1\" data-mce-src=\"https://cdn.shopify.com/s/files/1/0798/2303/files/love17.web_480x480.jpg?v=1634302667\"><br>\n</div>\n<div style=\"padding-left: 60px;\" data-mce-style=\"padding-left: 60px;\"></div>\n<h1 style=\"text-align: center;\" data-mce-style=\"text-align: center;\"></h1>\n<div class=\"kc-elm kc-css-330264 kc_col-sm-8 kc_column kc_col-sm-8\">\n<div class=\"kc-col-container\">\n<div class=\"kc-elm kc-css-772778 kc_text_block\">\n<h5 class=\"p2\" data-mce-style=\"padding-left: 30px;\"><strong></strong></h5>\n</div>\n</div>\n</div>\n<div style=\"text-align: center;\" data-mce-style=\"text-align: center;\">\n<h1 style=\"text-align: center;\" data-mce-style=\"text-align: center;\"></h1>\n</div>"""
    Sfd = StringFeildDensity()
    a = Sfd.zlib_zip(test_text)
    print(f"压缩后数据类型为: {type(a)}")
    print(Sfd.unzlib_zip(a))
