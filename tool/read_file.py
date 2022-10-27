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

if __name__ == '__main__':
    # D:\PycharmProjects\pytest_2022\tool/
    # print(ReadFile.project_directory)
    #
    # print(ReadFile.read_yaml('config/environment.yaml'))
    print(ReadFile.read_yaml('case/test.yaml'))