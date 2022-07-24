# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：excuteTime.py
@IDE ：PyCharm
@Time ： 2022-07-23 20:44
"""
import time

"""
需求 ：
    1- 需要知道每一个用例的执行时间
    2- 不能修改原代码，以及原始执行方式
方式：
    1- 闭包：函数内部可以定义函数，如果内部函数使用了外层函数的变量，则会产生闭包；在python中支持将函数作为对象使用，
    可以将函数挡成变量或返回值使用。
优化：
    1- 不改变原来的执行方式：test = show_time(test)  # test=inner 每一个需要新增功能的函数都需要加这一行代码，
    优化语法 @show_time 装饰器 等价于 函数名变量 = show_time(函数名)
"""


def show_time(func):  # 外函数
    def inner(*args, **kwargs):  # 内函数 *args, **kwargs
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print('接口执行耗时>>>', endTime - startTime)
        return result  # 这个返回值就是inner函数的返回值

    return inner  # 函数对象


@show_time  # 等价于 ---- test=show_time(test) 函数对象
def test(*args, **kwargs):  # eg：原始接口代码 *args, **kwargs
    print('----开始自动化测试----')
    time.sleep(1)


if __name__ == '__main__':
    test(100, )
