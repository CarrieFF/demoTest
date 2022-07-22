# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_mock.py
@IDE ：PyCharm
@Time ： 2022-07-22 18:31
"""
import requests

HOST = "http://127.0.0.1:9090"


# def test():
#     payload = {
#         "user_id": "sq001",
#         "goods_id": "1234",
#         "num": 1,
#         "amount": 100.8}
#     resp = requests.get(url=f'{HOST}/api/order/create/', json=payload)
#     print(resp.text)
def commit_order(inData):
    url = f'{HOST}/api/order/create/'
    payload = inData
    resp = requests.post(url, json=payload)
    return resp.json()


if __name__ == '__main__':
    testData = {
        'user_id': 'sq123456',
        'goods_id': '20200813'
    }
