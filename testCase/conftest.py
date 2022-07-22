# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：conftest.py
@IDE ：PyCharm
@Time ： 2022-07-18 12:13
"""
import pytest
from conf.config import NAME_PWD
from libs.shop import Shop
from libs.login import Login


# @pytest.fixture(scope='function', autouse=True)
# def start_running():
#     # ------------测试开始前环境
#     print('接口自动化测试开始执行')
#     yield
#     # 自动化执行之后，数据清除操作
#     print('自动化执行之后，数据清除操作')


# ----------------登录操作----------------
# 其他模块需要调用这个参数
@pytest.fixture(scope='session')
def login_init():
    _token = Login().login(NAME_PWD, getToken=True)
    yield _token  # 返回token
    print("--------登录完成-------------")


# ---------------店铺实例创建-------------------
@pytest.fixture(scope='class')
def shop_init(login_init):
    shopObject = Shop(login_init)
    yield shopObject  # 返回店铺实例

# -------------写成fixture-------------------------
 # with allure.step('1-用户登录+更新店铺'):
 #            pass
 #        with allure.step("2- 获取店铺id"):
 #            res = shop_init.query({'page': 1, 'limit': 10})
 #            shopID = res['data']['records'][0]['id']
 #        with allure.step('3- 文件上传操作'):
 #            res2 = shop_init.file_upload(os.path.join(testData_path, 'userImage.png'))
 #            fileInfo = res2['data']['realFileName']