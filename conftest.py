# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：conftest.py
@IDE ：PyCharm
@Time ： 2022-07-24 16:57
"""


# 处理pytest unicode的问题 标准写法conftest.py 不可随以改变，作用于整个根目录层级的文件
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
