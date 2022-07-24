# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：test_update.py   修改密码模块
@IDE ：PyCharm
@Time ： 2022-07-24 21:11
"""
import json
import os
import pytest, allure
import pytest_ordering
from common.baseAPI import BaseAPI
from utils.handle_excel import get_excel_data
from utils.handle_path import testData_path, report_path
from common.baseAPI import ApiAssert
from utils.handle_ini import conf

NAME_PWD = conf.get_str('test_data', 'NAME_PWD')
NAME_PWD = json.loads(NAME_PWD)


@allure.epic('接口自动化项目')
@allure.feature('修改密码模块')
@pytest.mark.retest
class TestUpdate:
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('title,bodyDate,expData', get_excel_data('修改密码', 'update', '标题', '请求参数', '响应预期结果'))
    @allure.story('修改密码')
    @allure.title("{title}")
    def test_updatepwd(self, title, bodyDate, expData, userinfo_init):
        with allure.step('1- 用户登录'):
            # testcase/conftest.py 前置已处理
            pass
        with allure.step('2- 修改用户密码'):
            pwd = bodyDate['password']
            resp = userinfo_init.update(bodyDate)
            # pwd = bodyDate['password']
            ApiAssert.denfine_api_assert(resp['code'], '=', expData['code'])
            if resp['code'] == 20000:
                with allure.step('3- 将用户密码修改到原始密码-数据回滚'):
                    bodyDate['oldPassword'] = pwd
                    bodyDate['password'] = NAME_PWD['password']
                    bodyDate['rePassword'] = NAME_PWD['password']
                    print(bodyDate)
                    resp = userinfo_init.update(bodyDate)
                    ApiAssert.denfine_api_assert(resp['code'], '=', expData['code'])
            else:
                pass

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('title,bodyDate,expData', get_excel_data('修改密码', 'logingout', '标题', '请求参数', '响应预期结果'))
    @allure.story('退出登录')
    @allure.title("{title}")
    def test_loginout(self, title, bodyDate, expData, userinfo_init):
        with allure.step('1- 用户登录'):
            pass
        with allure.step('2- 退出登录'):
            resp = userinfo_init.loginout()
            ApiAssert.denfine_api_assert(resp['code'], '=', expData['code'])


if __name__ == '__main__':
    pytest.main([__file__, '-sv', '-m', 'retest', '--alluredir', f'{report_path}', '--clean-alluredir'])
    os.system(f'allure serve {report_path}')
