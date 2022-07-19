# -*- coding: utf-8 -*-
# @Time : 2022/7/19 11:34
# @Author : Zhangzixu
# @Software: PyCharm
# @Description: Python 内置函数的使用
import loguru


class PythonBuiltInFunc:
    def __init__(self):
        """
        环境: python 3.6.8
        python 一共提供了68个内置函数主要作用于:
            * 数据类型
            进制转换
            * 数学运算
            * 数据结构相关: ["序列","集合"]
            ** 作用域
            ** 生成器与迭代器
            字符串代码执行
            输入输出
            内存相关
            文件操作相关
            模块相关
            帮助
            调用
        学习参考网站: https://cloud.tencent.com/developer/article/1950923
        """
        self.logger = loguru.logger

    def type_of_data(self):
        """
        数据类型
        Returns:
            None
        """
        self.logger.info(f"布尔值返回:{bool('布尔值')}")
        self.logger.info(f"整型返回:{int('123')}")
        self.logger.info(f"浮点型返回:{float('456.12')}")
        self.logger.info(f"复数返回:{complex(1, 2)}")

    def math_operation(self):
        """
        数学运算
        Returns:
            None
        """
        self.logger.info(f"abs绝对值:{abs(-2)}")
        self.logger.info(f"divmod返回商和余数:{divmod(20, 3)}")
        self.logger.error(f"**推荐** round四舍五入 :{round(3.1415926)}")
        self.logger.info(f"pow,求a的b次幂,第三个参数表示求幂之后进行取余:{pow(5, 3, 2)}")
        self.logger.info(f"sum求和:{sum([1, 2, 3])}")
        self.logger.debug(f"min最小值:{min(1, 2, 3)}")
        self.logger.debug(f"max最大值:{max(1, 2, 3)}")

    def data_structure(self):
        """
        数据结构
        目前仅列举几个方法,因为只有到了相应的使用场景,才知道如何去使用那些方法
        Returns:
            None
        """
        listA = [1, 2, 3, 4, 5, 6, 7, 8]
        stringA = "摩西摩西"
        self.logger.info(f"list转换:{list(stringA)}")
        self.logger.info(f"**使用场景少** reversed对列表反转之后:{list(reversed(stringA))}")
        s = slice(1, 3, 2)
        self.logger.info(f"**不推荐** slice就相当于预先确定好的切片方法:{listA[s]}")
        self.logger.info(f"**使用场景少** ord求字母或者字符在ASCLL码中的位置:{ord('a')}")
        self.logger.info("========= many more =========")

    def get_help(self, string):
        """
        针对传入的文本在python内置函数中进行搜索并给出相关联类/函数使用方法
        Args:
            string:传入文本

        Returns:
            类/函数的相关注释
        """
        self.logger.info(help(string))

    def class_attr(self):
        """
        操作类属性
        Returns:
            None
        """

        class Func1:
            name = "宝宝巴士"

        self.logger.info(f"获取Func1中的类属性:{getattr(Func1, 'name')}")
        self.logger.info(f"给Func1设置类属性:{setattr(Func1, 'name1', '惊雷')}")
        self.logger.info(f"获取Func1中的类属性:{getattr(Func1, 'name1')}")
        self.logger.info(f"Func1().xxx 等于 getattr(Func1,'xxx')")
        self.logger.error("Func1().xyz = 123 这种就不属于给类设置属性,无法通过getattr获取到")


if __name__ == '__main__':
    p = PythonBuiltInFunc()
    p.class_attr()
