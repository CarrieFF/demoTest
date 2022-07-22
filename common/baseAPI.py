# 给其他业务层类继承，如果子类有特殊需求，则重写父类方法
# -*- coding:utf-8 -*-
"""
基类的封装：
    1- 加入异常机制
    2- 截图操作 -UI 自动化
    3- 一般模块的常用接口
"""
import traceback

import requests
from utils.handle_yml import get_yaml_data
import inspect
import sys
from conf.config import HOST
from utils.handle_loguru import log

"""
import inspect
1- 可以获取类或函数的参数信息
2- 获取当前本函数的函数名
3- 获取调用函数的函数名
---------------------------------
关于token，公共鉴权的处理：
    1- 登录接口不用token
    2- 其他业务接口，需要使用token
"""


class BaseAPI:
    def __init__(self, token=None):  # 初始化方法
        # __class__.__name__ 获取类名 类名需要与yml的data模块同名
        # print("当前类名是", self.__class__.__name__)
        self.data = get_yaml_data('../conf/apiConfig.yml')[self.__class__.__name__]
        if token:
            self.headers = {'Authorization': token}
        else:
            self.headers = None

    # 通用的发送方法
    def request_send(self, data=None, json=None, param=None, files=None, id=''):  # json=None, param=None
        try:
            # 找到哪个函数调用了request_send方法
            methodName = inspect.stack()[1][3]
            # 将函数名作为data的key拿到对应的value（要求函数名与data中的key同名）
            path, method = self.data[methodName].values()
            resp = requests.request(method=method, url=f'{HOST}{path}' + str(id), data=data, headers=self.headers,
                                    json=json,
                                    params=param, files=files)
            print(f'request_send发送{methodName}请求，返回值{resp.json()}')
            return resp.json()
        except Exception as error:
            # 打印日志
            log.error(traceback.format_exc())
            raise error

    # 查询接口 get
    def query(self, bodyData):
        return self.request_send(param=bodyData)

    # 修改接口
    def update(self, bodyData):
        return self.request_send(data=bodyData)

    # 删除接口
    def delete(self, id):
        return self.request_send(id=id)

    # 增加接口
    def add(self, bodyData):
        return self.request_send(data=bodyData)

    # 文件上传 file：excel,image等等
    """
        遇到不怎么接触的接口时候，处理方式：
            1- 度娘
            2- 抓包观察接口特征
        请求参数：
            userFile={'变量名':(文件名,文件对象,文件类型)}
    """

    def file_upload(self, fileDir: str):  # d:/123.png
        # fileName=123.png, fileDir=d:/123.png, fileType=png
        fileName = fileDir.split('\\')[-1]
        fileType = fileName.split('.')[-1]
        userFile = {'file': (fileName, open(fileDir, mode='rb'), fileType)}
        return self.request_send(files=userFile)


# 断言类
class ApiAssert:
    @classmethod  # 类方法
    def denfine_api_assert(cls, result, condition, exp_result):
        try:
            if condition == "=":
                assert result == exp_result
            elif condition == "in":
                assert exp_result in result
        except Exception as error:
            # 打印日志
            log.error(traceback.format_exc())
            raise error

#
# def a():
#     print("执行函数A")
#     print("谁调用了我A，函数名是",inspect.stack()[1][3])
#
#
# def b():
#     print("执行函数B")
#     a()
#     # print('b函数----当前自己的函数名', sys._getframe().f_code.co_name)
#
# b()
