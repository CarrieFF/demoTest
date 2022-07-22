# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：login.py
@IDE ：PyCharm
@Time ： 2022-07-15 10:47
"""
from common.baseAPI import BaseAPI
from conf.config import NAME_PWD
from utils.handle_data import get_md5
import copy
import jsonpath

"""
    登录接口---使用场景：
        1- 登录
        2- 获取token
"""


class Login(BaseAPI):
    def login(self, bodyData, getToken=False):
        bodyData = copy.copy(bodyData)  # 浅拷贝数据，避免修改全局数据
        bodyData['password'] = get_md5(bodyData['password'])
        resp = self.request_send(data=bodyData)
        if getToken:
            # token = jsonpath.jsonpath(resp, '$..token')  ====》返回的token是个list类型
            token = resp['data']['token']
            return token
        else:
            return resp

    # def loginout(self):
    #     self.request_send()


if __name__ == '__main__':
    token = Login().login(NAME_PWD, getToken=True)
    print(token)
