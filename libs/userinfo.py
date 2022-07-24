# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：userinfo.py  处理用户信息模块的接口
@IDE ：PyCharm
@Time ： 2022-07-24 17:11
"""
from common.baseAPI import BaseAPI
from libs.login import Login
from utils.handle_data import get_md5
from utils.handle_ini import conf
import json, copy

NAME_PWD = conf.get_str('test_data', 'NAME_PWD')
NAME_PWD = json.loads(NAME_PWD)


class userInfo(BaseAPI):
    # 修改用户密码
    def update(self, bodyData):
        bodyData['oldPassword'] = get_md5(bodyData['oldPassword'])
        bodyData['password'] = get_md5(bodyData['password'])
        bodyData['rePassword'] = get_md5(bodyData['rePassword'])
        return super(userInfo, self).update(bodyData)  # 调用父类BaseAPI的update()

    # 退出登录
    def loginout(self):
        resp = self.request_send()
        return resp


if __name__ == '__main__':
    # 登录系统
    token = Login().login(NAME_PWD, getToken=True)
    # 创建userinfo实例
    userinfomation = userInfo(token)
    # 修改用户密码
    bodyData = {"oldPassword": "123456", "password": "22136", "rePassword": "22136"}
    resp1 = userinfomation.update(bodyData)
    print(resp1)
    # 退出登录
# result = userinfomation.loginout()
