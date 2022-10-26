# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/26/2022 1:21 PM
# 文件名称: __init__.py.PY
from config.config import Environment
from tool.read_file import ReadFile


def requests_environment_info(environment=Environment):
    '''
    :return: 返回ip和headers信息
    '''
    # 配置文件信息
    try:
        env_info = ReadFile.read_yaml('config/environment.yaml')
        # 测试环境配置文件相关信息
        request_info = env_info[environment]
        return {'ip': request_info['http'] + request_info['domain_name'], 'headers': request_info['headers']}
    except Exception as e:
        print(f'读取配置信息出错：{e}')

if __name__ == '__main__':
    #定义的时候是用的默认参数 调用的时候不指定也没关系
    # {'ip': 'http://192.168.11.177:8001', 'headers': {'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'token': 'em123dca666333'}}
    print(requests_environment_info())