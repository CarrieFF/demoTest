# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：login.py #  用于接口的调用
@IDE ：PyCharm
@Time ： 2022-07-15 10:47
"""
from common.baseAPI import BaseAPI
from utils.excuteTime import show_time
from utils.handle_data import get_md5
import copy
from utils.handle_ini import conf
# import jsonpath
import json

"""
    登录接口---使用场景：
        1- 登录
        2- 获取token
"""

NAME_PWD = conf.get_str('test_data', 'NAME_PWD')
NAME_PWD = json.loads(NAME_PWD)

class Login(BaseAPI):
    # @show_time
    def login(self, bodyData, getToken=False):
        bodyData = copy.copy(bodyData)  # 浅拷贝数据，避免修改全局数据
        bodyData['password'] = get_md5(bodyData['password'])
        resp = self.request_send(data=bodyData)
        if getToken:
            # token = jsonpath.jsonpath(resp, '$..token')  ====》返回的token是个list类型
            return resp['data']['token']
        else:
            return resp


if __name__ == '__main__':
    token = Login().login(NAME_PWD, getToken=True)
    print(token)
