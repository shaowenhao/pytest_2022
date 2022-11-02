# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/26/2022 3:37 PM
# 文件名称: requests_.PY
import requests
import json

from tool import requests_environment_info
from tool.log import logger

class Requests:
    @classmethod
    def get(cls, path):
        url = requests_environment_info()['ip'] + path
        headers = requests_environment_info()['headers']
        logger.info(f'{path}最终的请求参数：url信息:{url},headers信息:{headers}')
        print(f'url信息{url},headrs信息{headers}')
        # headers里有token的值
        return requests.get(url=url,headers=headers).json()

    @classmethod
    def post(cls,path,data):
        url = requests_environment_info()['ip'] + path
        headers = requests_environment_info()['headers']
        logger.info(f'{path}最终的请求参数：url信息:{url},headers信息:{headers},data信息:{data}')
        print(f'url信息{url},headrs信息{headers},data信息{data}')
        return requests.post(url=url,headers=headers,data=json.dumps(data)).json()

if __name__ == '__main__':
    Requests.get('/api/v2/getxxx')
    # data信息{'shaowenhao': 'man'}
    Requests.post('/api/v2/postxxxx',{'shaowenhao':'man'})