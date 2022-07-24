# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：test_login.py 登录模块
@IDE ：PyCharm
@Time ： 2022-07-15 15:02
"""

"""
    测试文件执行条件：
        1- 该业务层代码封装ok
        2- 需要自动化测试用例----数据驱动-使用指定文件类型做功能用例：
            1- excel
            2- word
            3- xmind
            4- yaml
            5- 数据库
        自动化用例选择：靠代码或工具
        
"""
import allure
from libs.login import Login
from utils.handle_excel import get_excel_data
from utils.handle_yml import get_yaml_caseData
import pytest
from utils.handle_path import report_path, testData_path
import os
from common.baseAPI import ApiAssert


@allure.epic('接口自动化项目')
@allure.feature('登录模块')
class TestLogin:
    @pytest.mark.parametrize('title,bodyData,expData', get_excel_data('登录模块', 'Login', '标题', '请求参数', '响应预期结果')) # 通过读取excel形式进行数据驱动
    # @pytest.mark.parametrize('title,bodyData,expData', get_yaml_caseData(
    #     os.path.join(testData_path, 'loginCase.yml')))   # 通过读取loginCase.yml形式进行数据驱动
    @allure.title("{title}")
    def test_login(self, title, bodyData, expData):
        res = Login().login(bodyData)
        ApiAssert.denfine_api_assert(res['code'], '=', expData['code'])
        # assert res['msg'] == expData['msg']


if __name__ == '__main__':
    pytest.main([__file__, '-sv', '--alluredir', f'{report_path}', '--clean-alluredir',])
    # os.system(f'allure serve {report_path}')

"""
常见问题：在浏览器里出现allure也没显示No data
allure工作原理：
    1- 特性：allure是java的一个应用---跨平台
    2- 工作原理：
        1- allure是显示数据-就相当于显示屏
        2- 需要pytest 运行自动化测试用例，生成json文件---具体的生成路径alluredir=存放json文件
        3- allure serve 存放json文件的路径

"""
