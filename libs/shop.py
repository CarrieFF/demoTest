# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：shop.py
@IDE ：PyCharm
@Time ： 2022-07-15 11:00
"""
from common.baseAPI import BaseAPI
from conf.config import NAME_PWD
from libs.login import Login
from utils.handle_path import testData_path
import os


class Shop(BaseAPI):
    """
     店铺更新接口，数据从用例文件去读，excel或者yaml
        1- id 需要代码里去更新 ----字典更新值
        2- 图片信息需要输入传入
    """

    def update(self, shopId, fileInfo, bodyData):
        if bodyData['id'] == "id不存在":  # 不更新id
            bodyData['id'] == '000'
        else:
            # 1- 更新店铺id
            bodyData['id'] = shopId
        # 2- 更新文件信息
        bodyData['image_path'] = fileInfo
        bodyData['image'] = f'/file/getImaStream?fileName={fileInfo}'
        return super(Shop, self).update(bodyData)  # 调用父类BaseAPI的update方法

    # def add(self):
    #     pass


if __name__ == '__main__':
    # 1- 登录操作
    token = Login().login(NAME_PWD, getToken=True)
    # 2- 创建店铺实例
    shop = Shop(token)
    # 3- 列出店铺
    bodyData = {'page': 1, 'limit': 10}
    result = shop.query(bodyData)
    # 4- 获取店铺id 拿的是第一个店铺的id [0]
    shopId = result['data']['records'][0]['id']
    print(f'店铺id>>>>>>{shopId}')
    # 5- 文件上传
    result2 = shop.file_upload(os.path.join(testData_path, 'userImage.png'))
    fileInfo = result2['data']['realFileName']
    print(f'图片信息为>>>>>>{fileInfo}', )
    # 6- 更新店铺信息
    updateShopData = {
        "name": "快乐魔法coffee",
        "address": "快乐星球1号店",
        "id": "3269",
        "Phone": "13176876632",
        "rating": "6.0",
        "recent_order_num": 100,
        "category": "甜品饮品/咖啡",
        "description": "满30减5，满60减8",
        "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
        "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
    }
    result3 = shop.update(shopId, fileInfo, updateShopData)
