# -*- coding: utf-8 -*-
# @Time : 2022/6/21 9:56
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:

# 根据时间限制函数启动次数
from datetime import datetime, timedelta


def timeguard(time_interval, default=None):
    def decorator(function):
        # For first time always run the function
        function.__last_run = datetime.min

        def guard(*args, **kwargs):
            now = datetime.now()
            if now - function.__last_run >= time_interval:
                function.__last_run = now
                return function(*args, **kwargs)
            elif default is not None:
                return default(*args, **kwargs)

        return guard

    return decorator


@timeguard(time_interval=timedelta(seconds=4), default=None)
def aprint():
    print(f"现在是 : {datetime.now()}")
    return "AAA"


if __name__ == '__main__':
    for i in range(20):
        print(aprint())