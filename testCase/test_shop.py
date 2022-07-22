# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：test_shop.py
@IDE ：PyCharm
@Time ： 2022-07-17 22:13
"""
import allure
import pytest
from libs.shop import Shop
from libs.login import Login
from conf.config import NAME_PWD
from common.baseAPI import BaseAPI, ApiAssert
from utils.handle_excel import get_excel_data
from utils.handle_path import testData_path, report_path
import os

"""
    方案1：
        1- 在每一个店铺的测试方法里增加Shop().xxx()
        问题：
            1- 每一个测试方法都有一个店铺类对应的实例
            2- token需要传递很多次
    方案2：
        1- Shop() 增加setup_class ---构建店铺的实例操作放进去，这个测试类里面公用一个实例
    问题： 
        1- 登录操作与店铺创建实例的操作，只能在店铺类中使用_token，后续其他模块需要登录，需要重复写一样的代码
    def setup_class(self):
        _token = Login().login(NAME_PWD, getToken=True)
        self.shop = Shop(_token)
    def teardown_class(self):
        print('----店铺模块初始化完成-----')
        
    方案3：
        1- 模块化剥离 fixture处理
           
        
"""


@allure.epic('接口自动化项目')
@allure.feature('我的商铺模块')
# 测试类标签
@pytest.mark.shop
class TestShop:
    def setup_class(self):
        _token = Login().login(NAME_PWD, getToken=True)
        self.shop = Shop(_token)

    # 1- 列出店铺
    @pytest.mark.skipif(2 > 1, reason='先不执行')
    @pytest.mark.shop_query  # 测试方法标签
    @pytest.mark.parametrize('title,bodyData,expData', get_excel_data('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    @allure.story('列出店铺')
    @allure.title("{title}")
    def test_shop_query(self, title, bodyData, expData, shop_init):
        resp = shop_init.query(bodyData)
        ApiAssert.denfine_api_assert(resp['code'], '=', expData['code'])

    # 2- 更新店铺
    @pytest.mark.shop_update  # 测试方法标签
    @allure.story('更新店铺')
    @allure.title("{title}")
    @pytest.mark.parametrize('title,bodyData,expData', get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    def test_shop_update(self, title, bodyData, expData, shop_init):
        with allure.step('1-用户登录+更新店铺'):
            pass
        with allure.step("2- 获取店铺id"):
            res = shop_init.query({'page': 1, 'limit': 10})
            shopID = res['data']['records'][0]['id']
        with allure.step('3- 文件上传操作'):
            res2 = shop_init.file_upload(os.path.join(testData_path, 'userImage.png'))
            fileInfo = res2['data']['realFileName']
        with allure.step('4- 更新店铺操作'):
            res3 = shop_init.update(shopID, fileInfo, bodyData)
        with allure.step('5- 断言'):
            ApiAssert.denfine_api_assert(res2['code'], '=', expData['code'])

    """
        流程化：一个业务包含很多个模块接口
        实例：变更接口---查询接口
        方案1：
            直接更新接口响应里就有对应的更新后的结果--可以直接断言这个接口的响应的关键信息
        方案2：
            1- 变更接口请求完没有任何有价值数据---可能返回return code 200-----不能直接断言
            2- 自动化测试肯定要断言：
                1- 使用查询接口查询获取的是一个列表数据，更新的内容(id),是否在列表数据里，是否更新
                2- 没有查询接口的情况 ，需要操作者操作数据库mysql等等
    
    """
    """
        一个：'-m','login'
        多个：'-m','login or shop_query'
        排除法：'-m','not shop_query'
        排除多个：'-m','not (login or shop_query)'
    """


if __name__ == '__main__':
    # pytest.main([__file__, '-sv', '-m', 'shop_query', '--alluredir', f'{report_path}', '--clean-alluredir'])
    pytest.main([__file__, '-sv', '--alluredir', f'{report_path}', '--clean-alluredir'])
    os.system(f'allure serve {report_path}')
