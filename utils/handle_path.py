# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_path.py
@IDE ：PyCharm
@Time ： 2022-07-15 16:55
"""
import os

"""
    需求：代码在任意路径都可以获取到项目工程路径
"""
# 项目工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置路径
conf_path = os.path.join(project_path, 'conf')

# 测试数据路径
testData_path = os.path.join(project_path, 'data')

# testCase路径
testCase_path = os.path.join(project_path, 'testCase')

# 测试报告路径
report_path = os.path.join(project_path, r'outFiles\report')

# log路径
log_path = os.path.join(project_path, r'outFiles\log')

# fileDir=os.path.join(testData_path,'userImage.png')
# print(fileDir)
