# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/26/2022 3:37 PM
# 文件名称: requests_.PY
import requests
import json

from tool import requests_environment_info


class Requests:
    @classmethod
    def get(cls, path):
        url = requests_environment_info()['ip'] + path
        headers = requests_environment_info()['headers']
        print(f'url信息{url},headrs信息{headers}')
        requests.get(url=url,headers=headers).json()

    @classmethod
    def post(cls,path,data):
        url = requests_environment_info()['ip'] + path
        headers = requests_environment_info()['headers']
        print(f'url信息{url},headrs信息{headers},data信息{data}')
        return requests.post(url=url,headers=headers,data=json.dumps(data)).json()

if __name__ == '__main__':
    Requests.get('/api/v2/getxxx')
    Requests.post('/api/v2/postxxxx')