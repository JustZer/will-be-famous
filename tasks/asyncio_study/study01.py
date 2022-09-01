# -*- coding: utf-8 -*-
# @Time : 2022/9/1 17:36
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:
"""
1. 协程的学习
    简介：协程部署于计算机提供的方法,而是程序员人为实现的功能

    协程：可以简称为 *微线程* ,是一种用户实现的上下文切换技术,总而言之就是实现代码块互相切换执行

    实现协程的方法:
    1. greenlet:早期模块
    2. yield 关键字
    3. asynico 装饰器 (py3.4+)
    4. async、await 关键字(py3.5+)【推荐使用】

2. 协程的意义
    如果在线程中遇到了IO等待时间,线程不会进行等待,而是利用空闲时间去做其他任务.


3. 事件循环
    可以理解成一个死循环去检测某些任务代码，将 “可执行” 与 “已完成”的任务返回，随后分别处理
    如果 “任务队列” 中的任务都已经完成，就跳出循环
    # 生成并获取一个事件循环
    loop = asyncio.get_event_loop()
    # 将任务放到任务列表
    loop.run_until_complete(任务)
    
3.2 快速上手
    协程函数。定义函数的时候 async def 函数名称。
    写成对象。执行 写成函数()得到的协程对象。
    注意：执行协程函数创建协程对象，函数内部代码不会执行。
    如果想要运行协程函数内部代码，必须要讲写成对象交给事件循环来处理。
    一般的方法：
        loop = asyncio.get_event_loop()
        loop.run_until_complete(任务)
    Py3.7+(本质上还是执行的 "一般方法" ):
        asyncio.run(任务)

3.3 await
    await + 可等待对象(协程对象，Future、Task对象 -> IO等待)
        只能跟可等待对象
    await 就是等待对象得到值之后才会继续执行下文.

3.4 Task 对象
    简介：在事件循环中添加多个任务

    【不是真正的并发,只是来回切换其他协程，执行的时间很接近】
     tasks用于并发调度协程，通过 asyncio。create_task(写成对象) 【Py3.7+】的方式创建 task 对象.
    这样可以让协程加入事件循环中等待被调度执行，除了使用 asyncio。create_task() 函数意外，还可以用底层级的 loop.creat_task() 或 ensure_future() 函数.不建议手动实例化task对象





"""
import asyncio


class GreenLetStudy:
    import greenlet

    def fun1(self):
        print(1)


class YieldStufy:
    """
    总的来说 yield 就是将代码进行了 “暂存” 操作,在一个函数执行途中进行暂停,随后切换去执行另一个代码
    yield 还是属于伪造的协程操作.实用性不高.
    Yields Returns
        iters 生成器
    """

    def func1(self):
        yield 1
        yield from self.func2()
        yield 2

    @staticmethod
    def func2():
        yield 3
        yield 4

    def main(self):
        f1 = self.func1()
        for item in f1:
            print(item)


class AsynicoStudy:
    """
    仅支持 Py3.4+ 版本
    牛逼之处在于: 如果遇见 I/O 堵塞,会自动切换协程
    """

    @asyncio.coroutine
    def func1(self):
        print(1)
        yield from asyncio.sleep(2)
        print(2)

    @asyncio.coroutine
    def func2(self):
        print(3)
        yield from asyncio.sleep(2)
        print(4)

    def main(self):
        tasks = [
            asyncio.ensure_future(self.func1()),
            asyncio.ensure_future(self.func2())
        ]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))


class AsyncAndAwait:
    """
    与 Asynico 使用相同,区别在于不使用装饰器,给函数前新增 async ,将 yield from 更改为 await 即可.
    """

    async def func1(self):
        print(1)
        await asyncio.sleep(2)
        print(2)

    async def func2(self):
        print(3)
        await asyncio.sleep(2)
        print(4)

    def main(self):
        tasks = [
            asyncio.ensure_future(self.func1()),
            asyncio.ensure_future(self.func2())
        ]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))


class TaskObjectStudy:
    """
    task 对象主要是给事件循环立即添加对象
    如果事件循环中存在IO等待的任务可以直接切入执行 task 的插入任务
    """

    async def func(self):
        print(1)
        await asyncio.sleep(2)
        print(2)
        return "I am Back"

    async def main(self):
        print("start.")

        # 创建 task 对象，将当前执行 func 函数任务添加到事件循环中.
        task1 = asyncio.ensure_future(self.func())
        # task1 = asyncio.create_task(self.func()) # Py3.7+

        # 创建 task 对象，将当前执行 func 函数任务添加到事件循环中.
        task2 = asyncio.ensure_future(self.func())
        # task2 = asyncio.create_task(self.func()) # Py3.7+

        print("end.")

        # 当执行某个协程遇到IO操作的说实话，会自动切换并执行其他任务
        # 此处的 await 是等待相应的协程全部执行完毕并获取结果
        res1 = await task1
        res2 = await task2
        print(res1, res2)

    async def main1(self):
        """
        第二种共同执行的方法
        Returns:

        """
        print("start.")

        task_list = [
            asyncio.ensure_future(self.func()),
            asyncio.ensure_future(self.func())
        ]

        print("end.")

        done, padding = await asyncio.wait(task_list, timeout= None)

        print(done)


if __name__ == '__main__':
    async_study = AsynicoStudy()
    async_study.main()
