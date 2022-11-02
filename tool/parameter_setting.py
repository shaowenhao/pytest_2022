# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 10/27/2022 1:37 PM
# 文件名称: parameter_setting.PY
from jsonpath import jsonpath


class ParameterSetting:
    # 参数池,保存接口返回参数提取出的值，提供给需要的接口请求参数使用
    access_value = {}

    @classmethod
    def data_is_replace(cls, data):
        '''
        :param data: 请求参数data和提取参数extract_key
        :return: 返回参数是否需要被替换
        '''
        if data is None:
            return False
        for k, v in data.items():
            if '$.' in v:
                return True
        return False

    @classmethod
    def parameter_setting(cls, data: dict, type='get'):
        '''
        :param data: 返回结果提取和参数依赖使用dict 例：{'bill': '$.bill'}
        :param type: save ：把数据存到参数池里面无返回，get读取参数池数据并返回新值
        :return:
        '''

        if type == 'save':
            # {'a':44,'a1':144} 键 + 明确的值
            for k, v in data.items():
                # 把data的键值添加到参数池里面
                cls.access_value[k] = v

        if type == 'get':
            # data={'b': '$.b','g':'$.g'} 提取格式键+提取表达式,这里处理参数提取
            for k, v in data.items():
                if '$.' in v:
                    if not jsonpath(cls.access_value, v):
                        return {'错误信息': '未读取到参数'}
                    v = jsonpath(cls.access_value, v)[0]
                    data[k] = v
            # # data={"time": random_time(),"str": random_str(6),"int": random_number(5)}
            # # ，这里处理函数(随机字符，随机数)
            # for k, v in data.items():
            #     if 'random' in str(v):
            #         data[k]=eval(v)
            print(f'最终返回的参数{data}')
            return data

    @classmethod
    def extract_value(cls,api_response:dict,extract_key:dict):
        '''

        :param api_response:
        :param extract_key: e.g. {'billCommonNo':'$.content.billCommonNo'}
        :return: 返回通过表达式提取出接口的最终要存的值
        '''
        # api_response = {'code':200,'billComminNo':'20221101'}
        extract_value = {}
        for k,v in extract_key.items():
            extract_value[k] = jsonpath(api_response,v)[0]
            #定义的参数池 返回明确的值 e.g. {'billCommonNo':'20221101'}
        return extract_value

if __name__ == '__main__':

    # 自测写入前后 准备一个字典类型的数据
    # {}
    # {'d': 999}
    a = {'d':999}
    print(ParameterSetting.access_value)
    ParameterSetting.parameter_setting(a,'save')
    print(ParameterSetting.access_value)

    # 最终返回的参数
    # {'ddd': 999}
    b = {'ddd':'$.d'}
    ParameterSetting.parameter_setting(b)