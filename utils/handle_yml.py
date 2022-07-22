import yaml


def get_yaml_data(fileDir):
    """
    :param fileDir: 文件路径
    :return: 返回yaml内容
    """
    with open(fileDir, 'r', encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())  # 使用yaml加载方法得到文件里内容


# ----------获取yaml用例的函数-------------
def get_yaml_caseData(fileDir):
    resList = []  # 存放结果[(标题,请求数据,响应数据)]
    res = get_yaml_data(fileDir)
    for one in res:
        resList.append((one['detail'], one['data'], one['resp']))
    return resList


if __name__ == '__main__':
    # res = get_yaml_data('../conf/apiConfig.yml')
    # print(res, type(res))
    #
    res = get_yaml_caseData('../data/loginCase.yml')
    print(res, len(res))
