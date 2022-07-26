# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_ini.py
@IDE ：PyCharm
@Time ： 2022-07-24 18:38
"""
from configparser import ConfigParser
import os
from utils.handle_path import conf_path


class MyConf:
    def __init__(self, fileName, encoding="utf-8"):
        """
        :param fileName:  配置文件名
        :param encoding: 文件编码方式
        """
        self.fileName = fileName
        self.encoding = encoding
        # 创建文件解析对象，读取配置文件
        self.conf = ConfigParser()
        self.conf.read(fileName, encoding='utf-8')

    def get_str(self, section, option):
        """
        :param section:配置块
        :param option:配置项
        :return:对应配置项的数据
        """
        return self.conf.get(section, option)

    def get_int(self, section, option):
        """
        读取数据
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """
        return self.conf.getint(section, option)

    def get_float(self, section, option):
        """
        读取数据
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """
        return self.conf.getfloat(section, option)

    def get_bool(self, section, option):
        """
        读取数据
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """
        return self.conf.getboolean(section, option)

    def write_data(self, section, option, value):
        """
        写入数据
        :param section: 配置块
        :param option: 配置项
        :param value:  配置项对应的值
        """
        # 写入内容
        self.conf.set(section, option, value)
        # 保存到文件
        self.conf.write(open(self.fileName, "w", encoding=self.encoding))


fileName_path = os.path.join(conf_path, "conf.ini")
conf = MyConf(fileName_path)

if __name__ == '__main__':
    print(conf.get_str("test_data", "NAME_PWD"))
