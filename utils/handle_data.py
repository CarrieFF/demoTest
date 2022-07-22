# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_data.py
@IDE ：PyCharm
@Time ： 2022-07-15 13:46
"""

import hashlib


def get_md5(pwd: str):
    """
    :param pwd: 加密前的密码
    :return: 加密后的密码
    """
    # 创建md5实例
    md5 = hashlib.md5()
    # 调用加密方法
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()
