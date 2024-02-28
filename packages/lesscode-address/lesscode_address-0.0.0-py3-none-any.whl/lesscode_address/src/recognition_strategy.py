import os

from lesscode_address import cpca
from lesscode_address.src.address_parser import Address_Parser
from lesscode_address.src.address_recognition import AddressIdentify, DATA_PATH

"""-----------------------------------------------------------------------------
Info: 抽取策略
-----------------------------------------------------------------------------"""


class RecognitionStrategy:

    def __init__(self):
        self.address_ident = AddressIdentify(os.path.join(DATA_PATH, 'address.csv'))
        self.address_parser = Address_Parser(os.path.join(DATA_PATH, 'areas.json'))

    def method_cpca(self, addr):
        """
           cpca方法
        """

        if type(addr) != str or len(addr) < 2:  # 对输入为nan和空字符串进行处理
            return ['', '', '']

        text_arr = {addr}
        df = cpca.transform(text_arr)

        province = df.iat[0, 0]
        city = df.iat[0, 1]
        district = df.iat[0, 2]

        if province == None:
            province = ''
        if city == None:
            city = ''
        if district == None:
            district = ''

        result = []
        result.append(province)
        result.append(city)
        result.append(district)

        return result

    def method_inverted_trie_tree(self, addr):
        """
            倒序trieTree方法
        """
        if type(addr) != str or len(addr) < 2:  # 对输入为nan和空字符串进行处理
            return ['', '', '']

        res = self.address_ident.address_match(addr)

        # 处理res=[]的情形
        if not res.__contains__('province'):
            return ['', '', '']

        result = []
        result.append(res['province'])
        result.append(res['city'])

        if res['county'] == '-1':
            res['county'] = ''

        result.append(res['county'])

        return result

    def method_address_parser(self, addr):
        """
            正序匹配方法
        """
        if type(addr) != str or len(addr) < 2:  # 对输入为nan和空字符串进行处理
            return ['', '', '']

        res = self.address_parser.parse(addr)

        result = []
        result.append(res[1])
        result.append(res[2])
        result.append(res[3])

        return result

    def strategy(self, addr, strategy='cpca-itt-add'):
        """
        解析组合策略
        :param addr:
        :param strategy: 'cpca-itt-add', 'add-itt-cpca'
        :return:
        """
        province = ''
        city = ''
        district = ''

        # 定义策略
        if strategy == 'cpca-itt-add':
            method1 = self.method_cpca
            method2 = self.method_inverted_trie_tree
            method3 = self.method_address_parser
        elif strategy == 'add-itt-cpca':
            method1 = self.method_address_parser
            method2 = self.method_inverted_trie_tree
            method3 = self.method_cpca
        else:
            method1 = self.method_inverted_trie_tree
            method2 = self.method_cpca
            method3 = self.method_address_parser

        # 使用method1解析
        result1 = method1(addr)

        # method1解析【省】【市】【区】全部正确的情况
        if (len(result1[0]) > 0 and len(result1[1]) > 0 and len(result1[2]) > 0):
            province = result1[0]
            city = result1[1]
            district = result1[2]
            # print("address:{}, province:{}, city:{}, district:{}".format(addr, province, city, district))

        # method1解析【省】【市】,但【区】解析不了的情况
        elif (len(result1[0]) > 0 and len(result1[1]) > 0 and len(result1[2]) == 0):
            # 使用address倒序法从新解析区
            result2 = method2(addr)

            # method2解析结果正确，补充【区】地址
            if ((result2[0] == result1[0]) and (result2[1] == result1[1])):
                province = result2[0]
                city = result2[1]
                district = result2[2]
                # print("address:{}, province:{}, city:{}, district:{}".format(addr, province, city, district))
            else:  # 区解析不了
                province = result1[0]
                city = result1[1]
                district = ''
                # print("address:{}, province:{}, city:{}, district:{}".format(addr, province, city, district))

        # cpca解析【省】,但【市】【区】解析不了的情况
        elif (len(result1[0]) > 0 and len(result1[1]) == 0 and len(result1[2]) == 0):
            # 尝试inverted_trie_tree和正序addr_parser方法处理两种情况
            result2 = method2(addr)
            result3 = method3(addr)

            if (result2[0] == result1[0]):  # 【省】相等表明itt解析正确，补充itt信息
                province = result2[0]
                city = result2[1]
                district = result2[2]
                # print("address:{}, province:{}, city:{}, district:{}".format(addr, province, city, district))
            elif (result3[0] == result1[0]):  # 【省】相等表明addr解析正确，补充addr信息
                province = result3[0]
                city = result3[1]
                district = result3[2]
                # print("address:{}, province:{}, city:{}, district:{}".format(addr, province, city, district))
            else:  # 【市】【区】都解析不了
                province = result1[0]
                city = ''
                district = ''
                # print("address:{}, province:{}, city:{}, district:{}".format(addr, province, city, district))
        else:  # 省市区都解析不了
            # print("address:{} cannot process.".format(addr))
            pass

        return province, city, district
