# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/28/2022 2:16 PM
# 文件名称: assert.PY
# ["'12' in '123'", '"ig" == "$.ig"']

class Assert:

    @classmethod
    def assert_response(cls, api_response:dict, assert_list:list):
        for i in assert_list:
            if '$.' in i:
                # String find 查找 
                wz = i.find('$')

