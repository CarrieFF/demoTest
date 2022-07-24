# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_loguru.py
@IDE ：PyCharm
@Time ： 2022-07-17 15:50
"""
from utils.handle_ini import conf
from loguru import logger
from utils.handle_path import log_path
from time import strftime
import os


class MyLog:
    __instance = None  # 单例实现
    __call_flag = True  # 控制init调用，如果调用过了就不用再调用

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_log(self):
        if self.__call_flag:  # 看是否被调用过
            __curdate = strftime('%Y%m%d-%H%M%S')
            logger.remove(handler_id=None)  # 关闭console输出
            logger.add(os.path.join(log_path, 'AutoInterface') + __curdate + '.log', encoding='utf-8',
                       retention=conf.get_str('log', 'retention'),  # 清理
                       rotation=conf.get_str('log', 'rotation'),  # 循环，达到指定大小后创建新的日志
                       format=conf.get_str('log', 'format'),  # 日志输出格式
                       compression=conf.get_str('log', 'compression'),  # 日志压缩格式zip
                       level=conf.get_str('log', 'level'))  # 日志级别
            self.__call_flag = False  # 如果调用过则设置为False 单例模式，避免造成多个日志文件
        return logger


log = MyLog().get_log()

if __name__ == '__main__':
    log.error('testing')
