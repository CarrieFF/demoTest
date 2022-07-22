# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_loguru.py
@IDE ：PyCharm
@Time ： 2022-07-17 15:50
"""
from configparser import ConfigParser
from loguru import logger
from utils.handle_path import log_path, conf_path
from time import strftime
import os


class MyLog():
    __instance = None  # 单例实现
    __call_flag = True  # 控制init调用，如果调用过了就不用再调用

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_log(self):
        if self.__call_flag:  # 看是否被调用过
            __curdate = strftime('%Y%m%d-%H%M%S')
            cfg = ConfigParser()
            cfg.read(os.path.join(conf_path, 'loguru.ini'), encoding='utf-8')
            logger.remove(handler_id=None)  # 关闭console输出
            logger.add(os.path.join(log_path, 'AutoInterface') + __curdate + '.log', encoding='utf-8',
                       retention=cfg.get('log', 'retention'),  # 清理
                       rotation=cfg.get('log', 'rotation'),  # 循环，达到指定大小后创建新的日志
                       format=cfg.get('log', 'format'),  # 日志输出格式
                       compression=cfg.get('log', 'compression'),  # 日志压缩格式zip
                       level=cfg.get('log', 'level'))  # 日志级别
            self.__call_flag = False  # 如果调用过则设置为False 单例模式，避免造成多个日志文件
        return logger


log = MyLog().get_log()

if __name__ == '__main__':
    log.error('testing')
