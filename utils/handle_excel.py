# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_excel.py
@IDE ：PyCharm
@Time ： 2022-07-15 15:32
"""
import json
import xlrd
import os
from utils.handle_path import testData_path


def get_excel_data(sheetName, caseName, *args, runCase=['all'], excelDir=None):
    """
    :param excelDir: 用例文件路径
    :param sheetName: 选择sheet表
    :param caseName: 用例名
    :param args: 获取的列数据
    :param runCase: 选择运行的case
    :return:
    """

    """
        1- 操作Excel库的时候：
            1- xlrd 读 xlwt 写   操作xx.xls ----选定
            2- openpyxl 操作xx.xlxs
            3- panda 大数据场景
    """
    excelDir = os.path.join(testData_path, 'Delivery_System_V1.5.xls')
    resList = []  # 存放结果
    # 1- 打开文件 formatting_info=True保持原样视图
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)
    # # 2- 获取所有子表sheet名称
    # sheets = workBook.sheet_names()
    # 3- 获取所需要操作的sheet表
    workSheet = workBook.sheet_by_name(sheetName)
    # 获取第一列数据workSheet.col_values(0)，获取第一行数据workSheet.row_values(0)
    # 获取单元格数据workSheet.cell(行编号,列编号).value

    """
        *arg ---->元组类型(url,title,body)
        1- get_excel_data(excelDir, sheetName, caseName, *args)  
        2- get_excel_data(excelDir, sheetName, caseName, url,title,body)  

        第一种代码可读性差
        第二种代码操作更来方便 ---扩展性更好

                ----用例执行筛选：
                pytest框架的定制华执行：
                    1- mark 指定对应的接口跑自动化--不能选择里边的某一条用例
                    2- 数据层定制，数据驱动，我们筛选出我们需要执行的用例
                用例选择的方式：
                    1- 全部跑
                    2- 只选择某一个用例 ['login001']
                    3- 连续的用例 ['login001-login005']
                    4- 复合型 ['login001','login003-login005','login8']  
                    用例有all则运行所有case，其他条件失效
    """

    # runCase = []  # 运行用例编号 ['001','002','004-007','all']
    runList = []  # 运行用例编号列表 ['login001','login003-login005']
    if 'all' in runCase:
        runList = workSheet.col_values(0)  # 全部选择

    else:
        # 连续case [login003-login005]
        # 不连续case [login003,login005]
        # 组合case [login001, login003-login005]
        for k in runCase:
            if '-' in k:  # 连续的---->拿到区间内的用例所有编号
                start, end = k.split('-')  # 004,007----闭区间
                for l in range(int(start), int(end) + 1):
                    runList.append(caseName + f'{l:0>3}')  # ['login003','login004','login005']
            else:  # 不连续 004,008   /   4,8
                runList.append(caseName + f'{k:0>3}')  # 这里也可以不用补齐，如果已经有3位则不会再补了，没有的话会补齐，兼容下而已
                pass

        pass
    # 存放输入列名对应的编号
    colIndexList = []
    for i in args:  # (url,title,body) 遍历tuple
        colIndexList.append(workSheet.row_values(0).index(i))  # 获取参数在sheet中第一行数据中的下标
    rowIndex = 0  # 行编号初始值
    for one in workSheet.col_values(0):
        if caseName in one and one in runList:  # 筛选用例
            # 遍历列名对应的下标
            getColData = []
            for num in colIndexList:
                tmp = workSheet.cell(rowIndex, num).value
                if is_json(tmp):
                    tmp = json.loads(tmp)
                getColData.append(tmp)
            resList.append(list(getColData))
            # reqBody = workSheet.cell(rowIndex, 9).value  # 请求body
            # respData = workSheet.cell(rowIndex, 11).value  # 响应数据
            # resList.append((reqBody, respData))  # [(请求1,响应1)，(请求2.响应2)]
        rowIndex += 1  # 更新行编号，换下一行继续
    return resList


"""
    excel获取的出来是字符串，测试对结果进行判断时，都要转成字典dict
            1- 业务登录接口需要请求数据是dict格式，但是get_excel_data()返回的是字符串，需要转化 json.loads()
            2- 其他数据(URL,标题)本身就是字符串，不用转化
        优化建议：
            1- 加判断是否json格式      
"""


def is_json(inData: str):
    try:
        json.loads(inData)
        return True
    except:
        return False

#
# if __name__ == '__main__':
#     fileDir = os.path.join(testData_path, 'Delivery_System_V1.5.xls')
#     get_excel_data(fileDir, '登录模块', 'Login', 'URL', '请求参数', runCase=['1', '4-5', '6', 'all'])
