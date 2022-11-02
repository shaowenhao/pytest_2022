# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 11/2/2022 9:46 AM
# 文件名称: test_case.PY
import pytest

from tool import  ReadFile
from tool.case import case_assert_result
from tool.log import logger

@pytest.mark.parametrize('case_data',ReadFile.read_case('case/test.yaml'))
def test_case(case_data):
    logger.info(f'用例初始信息{case_data}')
    print(case_data)
    assert case_assert_result(case_data)
'''
tool/test_case.py::test_case[case_data0] {'path': '/get_waybill_no', 'method': 'get', 'remark': '获取运单号，提取运单号,这个方法提取出运单号', 'is_run': True, 'data': None, 'extract_key': {'waybill_no': '$.waybill_no'}, 'assert_expression': ['"lj520"=="$.waybill_no"'], 'case_name': '获取运单号'}
url信息http://192.168.1.5:8001/get_waybill_no,headrs信息{'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'token': 'em123dca666333'}
['"lj520"=="lj520"']
[True]
PASSED
tool/test_case.py::test_case[case_data1] {'path': '/lu_dan', 'method': 'post', 'remark': '录单，使用运单号', 'is_run': True, 'data': {'waybill_no': '$.waybill_no', 'lu_dan_ren': '小江'}, 'extract_key': None, 'assert_expression': ['"运单创建成功"=="$.msg"'], 'case_name': '录单'}
最终返回的参数{'waybill_no': 'lj520', 'lu_dan_ren': '小江'}
url信息http://192.168.1.5:8001/lu_dan,headrs信息{'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'token': 'em123dca666333'},data信息{'waybill_no': 'lj520', 'lu_dan_ren': '小江'}
['"运单创建成功"=="运单创建成功"']
[True]
PASSED

第一个接口返回值
{
    "waybill_no": "lj520"
}

第二个接口的返回值
{
    "msg": "运单创建成功",
    "waybill_info": {
        "waybill_no": "lj520",
        "lu_dan_ren": "小江"
    }
}
'''
