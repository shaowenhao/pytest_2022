# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/28/2022 2:16 PM
# 文件名称: assert.PY
# 需要断言的格式 ["'12' in '123'", '"ig" == "$.ig"']
from jsonpath import jsonpath


class Assert:

    @classmethod
    def assert_response(cls, api_response:dict, assert_list:list):
        '''
        :param api_response:  {'ig':'theshy','code':200}
        :param assert_list:
        :return:
        '''
        new_assert_list = []
        for i in assert_list:
            if '$.' in i:
                # String find 查找  获取$的索引位置
                wz = i.find('$')
                #切片出表达式
                assert_json_path = i[wz:len(i)-1]
                #把表达式转化为值
                value = jsonpath(api_response,assert_json_path)
                if not value:
                    print('表达式提取失败，请检查')
                    return False
                #得到的结果是放在列表里的 [theshy]
                value = value[0]
                #用值把表达式替换掉
                i = i.replace(assert_json_path,value)
            new_assert_list.append(i)
            #到这步位置 结果变成 ["'12' in '123'", '"ig" == "theshy"']
        assert_result_list = []
        for i in new_assert_list:
            assert_result = eval(i)
            assert_result_list.append(assert_result)
            #变成[True,False]
        print(new_assert_list)

        print(assert_result_list)
        if False in assert_result_list:
            return False
        return True

    #自测下
if __name__ == '__main__':
    # api_response = {'msg':'请求成功','ig':'theshy'}
    api_response = {'msg':'请求成功','ig':'ig'}
    assert_list = ["'12' in '123'",'"ig" == "$.ig"','1==1']
    print(Assert.assert_response(api_response,assert_list))






