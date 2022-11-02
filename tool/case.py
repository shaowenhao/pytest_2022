# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 11/1/2022 3:03 PM
# 文件名称: case.PY
# 把参数操作，断言操作，请求操作结合起来 返回最终的用例执行结果

from tool.requests_ import Requests
from tool.parameter_setting import ParameterSetting
from tool.assert_ import Assert

def extract_(api_response, extract_key):
    #参数提取
    if extract_key:
        extract_value = ParameterSetting.extract_value(api_response, extract_key)
        ParameterSetting.parameter_setting(extract_value, 'save')

def case_assert_result(case_data):
    if case_data['method'] == 'get':
        api_response = Requests.get(case_data['path'])
        extract_key = case_data['extract_key']
        # 可以优化 判断是否需要参数提取
        extract_(api_response, extract_key)
        assert_r = Assert.assert_response(api_response,case_data['assert_expression'])
        return assert_r

    elif case_data['method'] == 'post':
        #参数依赖
        if ParameterSetting.data_is_replace(case_data['data']):
            data = ParameterSetting.parameter_setting(case_data['data'],'get')
        data = case_data['data']
        api_response = Requests.post(case_data['path'],data)
        extract_key = case_data['extract_key']
        extract_(api_response, extract_key)
        assert_r = Assert.assert_response(api_response, case_data['assert_expression'])
        return assert_r




