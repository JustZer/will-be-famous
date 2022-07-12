# -*- coding: utf-8 -*-
# @Time : 2022/7/12 18:33
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:


class LogTest:
    def __init__(self):
        pass

    @staticmethod
    def use_loguru():
        """
        1. 自带高亮彩色 <允许自定义>
        2. 无需配置,使用简单 <允许自设置配置>
        3. 可以直接输出函数作用域与代码行数
        4. 自带多线程安全
        5. 可添加参数极多,涉及面广: 多进程(需添加 enqueue 参数)
                                Backtrace 参数实现堆栈梳理(支持函数参数还原)
                                日志压缩(需添加 compression 参数 -> ="zip")
                                日志滚动(需添加 rotation 参数 -> ="1 MB" 或者 ="12:00"(代表着每天12点将创建新的Log日志文件))
        官方文档: https://pypi.org/project/loguru/
        Returns:
            None
        """
        import loguru

        loguru.logger.info("# loguru #这是 INFO 输出")
        loguru.logger.debug("# loguru #这是 DEBUG 输出")
        loguru.logger.warning("# loguru #这是 WARNING 输出")
        loguru.logger.error("# loguru #这是 ERROR 输出")

        try:
            # 日志追溯功能
            # 也可以设置 Backtrace 参数实现相同效果
            @loguru.logger.catch()
            def get_error(x, y, z):
                return x / y / z

            get_error(1, 2, 0)
        except Exception as e:
            # 可以输出具体的行数以及上下文代码 <还不错>
            loguru.logger.exception(e)

        # 代码输出至文件
        loguru.logger.add("file_demo_{time}.log")
        loguru.logger.info("# loguru # 这是文件输出测试..")

    @staticmethod
    def use_logging():
        """
        1. 全面
        Returns:
            None
        """
        import logging
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s",
            # datefmt="%Y-%m-%d %H:%M:%S",
            # filename="demo.log",
            # filemode="w"
        )
        logging.info("# Logging # 这是 INFO 输出")
        logging.debug("# Logging # 这是 DEBUG 输出")
        logging.warning("# Logging # 这是 WARNING 输出")
        logging.error("# Logging # 这是 ERROR 输出")


if __name__ == '__main__':
    lt = LogTest()
    lt.use_loguru()
