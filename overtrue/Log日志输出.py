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

        loguru.logger.info("# loguru # info 表示程序正常运行,输出常规日志")
        loguru.logger.debug("# loguru # debug 表示正在调试运行程序,将输出很详细的日志")
        loguru.logger.warning("# loguru # warning 表示程序发生了一些意外,但是依旧可以正常工作")
        loguru.logger.error("# loguru # error 表示程序出现严重问题,这个软件已经不能执行部分功能了")
        loguru.logger.critical("# loguru # critical 表示程序已经无法正常运行")

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
        1. 应用方面全
        2. 熟知配置的使用需要一定的时间积累
        相关学习文档: https://www.cnblogs.com/jack-nie-23/p/16465791.html
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
        # 创建 logger 实例
        #   在不创建实例的情况下,会使用默认实例(root logger)
        logger = logging.getLogger("logger_name_v1")

        logger.info("# Logging # info 表示程序正常运行,输出常规日志")
        logger.debug("# Logging # debug 表示正在调试运行程序,将输出很详细的日志")
        logger.warning("# Logging # warning 表示程序发生了一些意外,但是依旧可以正常工作")
        logger.error("# Logging # error 表示程序出现严重问题,这个软件已经不能执行部分功能了")
        logger.critical("# Logging # critical 表示程序已经无法正常运行")

        try:
            raise ValueError
        except Exception as e:
            logger.exception(e)

if __name__ == '__main__':
    lt = LogTest()
    lt.use_logging()
