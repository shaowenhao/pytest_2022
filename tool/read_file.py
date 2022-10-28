# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/26/2022 1:23 PM
# 文件名称: read_file.PY
from pathlib import Path

import yaml


class ReadFile:
    # 当前项目的绝对路径
    project_directory = str(Path(__file__).parent.parent) + '/'

    @classmethod
    def read_yaml(cls, path):
        '''读取yaml文件，以字典格式返回{'用例标题':{'path':'/test','data':{'id':1}}}'''
        path = cls.project_directory + path
        file = open(path, 'r', encoding='utf-8')
        with file as doc:
            content = yaml.load(doc, Loader=yaml.Loader)
            return content

    @classmethod
    #根据case的定义 把case名加到内容部分的字典内容里
    def read_case(cls, path):
        case_data = cls.read_yaml(path)
        for k,v in case_data.items():
            case_name = k
            if v['is_run']:
                # 字典里多了一个K,V 'case_name': '获取运单号'
                v['case_name'] = case_name
                # 不要一次性返回所有的值 不用return 用yield
                #print(v)
                yield v

if __name__ == '__main__':
    # D:\PycharmProjects\pytest_2022\tool/
    # print(ReadFile.project_directory)
    #
    # print(ReadFile.read_yaml('config/environment.yaml'))
    # print(ReadFile.read_yaml('case/test.yaml'))

    # {'path': '/get_waybill_no', 'method': 'get', 'remark': '获取运单号，提取运单号,这个方法提取出运单号', 'is_run': True, 'data': None,
    #  'extract_key': {'waybill_no': '$.waybill_no'}, 'assert_expression': ['"lj520"=="$.waybill_no"'],
    #  'case_name': '获取运单号'}
    # {'path': '/lu_dan', 'method': 'post', 'remark': '录单，使用运单号', 'is_run': True,
    #  'data': {'waybill_no': '$.waybill_no', 'lu_dan_ren': '小江'}, 'extract_key': None,
    #  'assert_expression': ['"运单创建成功"=="$.msg"'], 'case_name': '录单'}
    case_data = ReadFile.read_case('case/test.yaml')
    for case in case_data:
        print(case)