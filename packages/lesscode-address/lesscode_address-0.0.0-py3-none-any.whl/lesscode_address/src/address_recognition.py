#! -*- coding:utf-8 -*-
import collections
import copy
import importlib
import json
import os
import re

try:
    pd = importlib.import_module("pandas")
except ImportError:
    raise Exception("pandas is not exist,run:pip install pandas")

"""-----------------------------------------------------------------------------
Info: 配置信息
-----------------------------------------------------------------------------"""

chinese_regex = 'u[^\u4e00-\u9fa5]'
EN = re.compile('[a-zA-Z]+')

PUNCTUATION = re.compile('[，。？！,.?!]|\s')

REGEX = re.compile(
    '(自治区|工业园|开发区|街道|社区|东区|地区|园区|省|市|区|县|镇|乡|村|庄|城)$|[一二三四五六七八九十]路')

BLACK_LIST = ['经济', '华林', '公司', '物流', '路南', '路东', '环路', '家园', '西外', '环路', '南段', '中心', '工业',
              '路西', '科技', '农业', '大学', '路北', '中路', '广场', '二路', '国际', '集团', '大道', '市东', '南路',
              '南岸']

BLACK_LIST_SEG = ['市南', '市北']

WHITE_LIST = ['歙', '淇', '荣', '息', '范', '吉', '攸', '米', '沙', '和', '曹', '易', '莘', '理', '滦', '澧', '威',
              '泸', '成', '浚', '富', '湘', '大', '徽', '赵', '横', '环', '铁', '嵩', '彬', '陇', '城', '义',
              '盂', '眉', '冠', '城', '绿', '岷', '寿', '唐', '勉', '单', '索', '户', '忠', '青', '揭', '磁', '河',
              '朗', '乾', '矿', '莒', '隰', '沧', '阳', '任', '蒲', '杞', '房', '沁', '盘', '藤', '兴', '临', '黟',
              '漳', '桥', '康', '洋', '景', '茂', '珙', '代', '赣', '金', '古', '新', '礼', '夏', '凤', '渠', '温',
              '乃', '芒', '蔚', '佳', '沛', '郏', '萧', '滑', '宾', '云', '郫', '魏', '丰', '文', '道', '绛',
              '宁', '颍', '郊', '梁', '江', '泾', '祁', '蠡', '卫', '泗', '费', '睢', '岚', '叶', '雄', '随']

SOURCE_PATH = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(SOURCE_PATH, 'dict/')

"""-----------------------------------------------------------------------------
Info: 采用萃树的方式构建词表
-----------------------------------------------------------------------------"""


class TrieTree(object):
    """
    字典树(TrieTree)，又称单词查找树或键树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计和排序
    大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。

    Trie的核心思想是空间换时间。利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。

    它的优点是：最大限度地减少无谓的字符串比较，查询效率比哈希表高。

    它有3个基本性质：
        (1) 根节点不包含字符，除根节点外每一个节点都只包含一个字符。
        (2) 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
        (3) 每个节点的所有子节点包含的字符都不相同。
    """

    def __init__(self, word_list=None, compact=False):
        self.tree = {'root': {}}
        self.root = -1
        if word_list:
            self.add_words(word_list)
        if compact:
            new_tree = {}
            self.compacted_tree(self.tree, new_tree)
            self.tree = new_tree

    def add_words(self, words_list):
        for index, word in enumerate(words_list):
            self.add_word(word)

    def add_word(self, word):
        tree = self.tree['root']
        for char in word:
            if char in tree:
                # tree['is_root'] = -1
                tree = tree[char]
            else:
                tree[char] = {}
                tree = tree[char]
                # tree['is_root'] = 1

    """压缩树"""

    def compacted_tree(self, old_tree, new_tree, new_key=''):
        for key, value in old_tree.items():
            new_key += key
            if not value:
                new_tree[new_key] = value
                new_key = ''
            elif len(value) > 1:
                new_tree[new_key] = {}
                next_tree = new_tree[new_key]
                new_key = self.compacted_tree(value, next_tree, '')
            else:
                sub_key = list(value.keys())[0]
                sub_tree = list(value.values())[0]
                new_key += sub_key
                if not sub_tree:
                    new_tree[new_key] = {}
                    new_key = ''
                else:
                    new_key = self.compacted_tree(sub_tree, new_tree, new_key)
        return new_key

    def is_has_word(self, word):
        local_tree = self.tree['root']
        for char in word:
            if char in local_tree:
                local_tree = local_tree[char]
            else:
                return False
        return True

    def save(self, path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.tree, f, ensure_ascii=False)

    def load(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            word_tree = json.load(f)
        self.tree = word_tree


"""-----------------------------------------------------------------------------
Info: 采用萃树的方式构建词表
-----------------------------------------------------------------------------"""


class DataProcess(object):
    """
        构建词表
    """

    def __init__(self, data):
        self.documents = collections.defaultdict(list)
        self.vocabulary = []
        if data is not None:
            self.__build_vocab(data)

    def __build_vocab(self, data: list):
        vocabulary = []
        for index, doc in enumerate(data):
            doc = re.sub(chinese_regex, '', str(doc))
            doc = re.sub(REGEX, '', doc)
            words = [item for item in list(doc)]
            self.documents[str(index)] = words
            vocabulary.extend(words)
        word_count = collections.Counter(vocabulary)
        self.vocabulary = list(word_count.keys())


class InvertedIndex(DataProcess):
    """
        倒排索引
    """

    def __init__(self, data=None, path=None):
        super(InvertedIndex, self).__init__(data)
        self.word_index = {word: [] for word in self.vocabulary}
        if path:
            self.load(path)
        else:
            self.__build_index()

    def __build_index(self):
        """构建索引"""
        for k, doc in self.documents.items():
            counter = collections.Counter(doc)
            for word in counter.keys():
                if word not in self.word_index:
                    continue
                self.word_index[word].append(k)

    def save(self, path):
        """save"""
        state = {
            'word_index': self.word_index,
            # 'vocabulary': self.vocabulary,
            # 'documents': self.documents
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False)

    def load(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            state = json.load(f)
        # self.vocabulary = state['vocabulary']
        # self.documents = state['documents']
        self.word_index = state['word_index']

    def search(self, query: str):
        """问句索引"""
        indexes = []
        for word in query:
            # index = [item['document_ID'] for item in self.word_index.get(word, {}) if item]
            index = self.word_index.get(word, [])
            if not index:
                continue
            if not indexes:
                indexes = index
                continue
            indexes = list(set(indexes).intersection(set(index)))

        if not indexes:
            return []
        docs = [(''.join(self.documents[index]), index) for index in indexes]
        return docs

    def run(self, query):
        """主接口"""
        query = re.sub(REGEX, '', query)
        if query in BLACK_LIST or (len(query) <= 1 and query not in WHITE_LIST):
            return []
        docs = self.search(query)
        if not docs:
            return []
        texts = list(set([text for text, _ in docs]))
        # if len(texts) > 20:
        #    print(query)
        texts = [text for text in texts if re.search(query, text)]
        try:
            Levenshtein = importlib.import_module("Levenshtein")
        except ImportError:
            raise Exception(f"python-Levenshtein is not exist,run:pip install python-Levenshtein==0.12.2")
        similarity = {text: Levenshtein.ratio(''.join(query), text) for text in texts}
        docs_collections = collections.defaultdict(list)
        for doc, index in docs:
            if doc in texts:
                docs_collections[doc].append(index)
        docs_collections = [{'words': key, 'indexes': value, 'score': similarity[key]}
                            for key, value in docs_collections.items()]
        # docs_collections = sorted(docs_collections, key=lambda x: x['score'], reverse=True)
        return docs_collections


"""-----------------------------------------------------------------------------
Info: 采用最大正向匹配算法做机械分词
-----------------------------------------------------------------------------"""


class Segment(object):
    def __init__(self, words_path=None):
        self.tree = TrieTree()
        if words_path:
            self.load_word_tree(words_path)

    def load_word_tree(self, path):
        self.tree.load(path)

    def build_word_tree(self, word):
        self.tree.add_word(word)

    def segment(self, sentence, seg_len=4):
        sentence = re.sub(chinese_regex, '', sentence)
        start = 0
        part = sentence[start:seg_len]

        while True:
            seg_words, position = self.part_segment(part)
            if seg_words in BLACK_LIST_SEG:
                position = position - (len(seg_words) - 1)
                seg_words = seg_words[0]

            if len(seg_words) > 1:
                yield {'words': seg_words, 'offset': (start, start + position)}

            start += position
            part = sentence[start:start + seg_len]

            if start >= len(sentence):
                break

    def part_segment(self, part_sentence):
        position = len(part_sentence)
        while True:
            if self.tree.is_has_word(part_sentence) or part_sentence == '*' or len(part_sentence) == 1:
                break
            position -= 1
            part_sentence = part_sentence[:position]

        return part_sentence, position


"""-----------------------------------------------------------------------------
Info: 中文地址识别
-----------------------------------------------------------------------------"""


class Address(object):
    def __init__(self, path):
        self.path = path
        self.address = pd.read_csv(path)

    def add(self, data: pd.DataFrame, saved_path=None):
        """添加数据"""
        if not isinstance(data, pd.DataFrame):
            print('type of added data must be DataFrame!')
            return False
        self.address = pd.merge(self.address, data, how='outer')
        if saved_path:
            self.address.to_csv(saved_path, index=False, encoding='utf_8_sig')

    def select_index(self, index: list):
        """根据索引筛选数据"""
        return self.address.iloc[index]

    def select_column(self, column, value: list):
        """根据列的值筛选数据"""
        return self.address[self.address[column].isin(value)]


class AddressIdentify(Address):
    '''
        地址识别
    '''

    def __init__(self, path):
        super(AddressIdentify, self).__init__(path)
        # self.rank2num = {'province': 1, 'city': 2, 'county': 3, 'town': 4, 'village': 5}
        self.rank2num = {'province': 1, 'city': 2, 'county': 3, 'town': 4}
        self.num2rank = {value: key for key, value in self.rank2num.items()}
        self.retrieval_model = {}
        self.segment_model = {}
        self.load_model()

    def load_model(self):
        for key in self.rank2num.keys():
            data = self.address[key]
            self.retrieval_model[key] = InvertedIndex(data=data,
                                                      path=os.path.join(DATA_PATH, 'retrieval_{}.json').format(key))
            self.segment_model[key] = Segment(words_path=os.path.join(DATA_PATH, '{}_tree.json').format(key))

    def address_match(self, s):
        """地址匹配"""
        # 区域匹配
        address_segment = []
        for key in self.rank2num.keys():
            s = copy.copy(s)
            segment_model = self.segment_model[key]
            segment_result = list(segment_model.segment(s, seg_len=10))
            if not segment_result:
                continue
            last_item = {'words': '', 'offset': (-1, -1)}
            segment_new = []
            for item in segment_result:
                item['rank'] = key
                # 去除重复词
                if last_item['words'] == item['words'] and (item['offset'][0] - last_item['offset'][1]) <= 3:
                    last_item = item
                    continue

                segment_new.append(item)
                last_item = item
            address_segment.append(segment_new)

        if not address_segment:
            return {}

        # 地址排列
        ranging = []
        for address in address_segment:
            ranging = self.address_rank(address, ranging)

        # # 过滤长度为1但级别不是小区级的
        # def fun(l):
        #     if len(l) == 1 and l[0]['rank'] != 5:
        #         return False
        #     return True
        # ranging = list(filter(fun, ranging))

        # 按长度进行排列
        ranging_by_length = collections.defaultdict(list)
        for item in ranging:
            length = len(item)
            ranging_by_length[length].append(item)
        ranging_by_length = collections.OrderedDict(sorted(ranging_by_length.items(), key=lambda x: x[0], reverse=True))

        # 地址校验
        words_indexes = {}
        for item in address_segment:
            words = [elem['words'] for elem in item]
            rank = item[0]['rank']
            indexes = self.get_index(words, rank)
            words_indexes[rank] = indexes

        checking_result = []
        for _, value in ranging_by_length.items():
            for address in value:
                result = []
                for rank_address in address:
                    rank = rank_address['rank']
                    word = rank_address['words']
                    offset = rank_address['offset']
                    match_res = words_indexes[rank].get(word, [])
                    if not match_res:
                        result = []
                        break
                    result = self.address_checking(result, match_res, rank, offset)
                    if not result:
                        break
                checking_result.extend(result)
            if checking_result:
                break

        # 去除offset为-1的值
        checking_result = list(filter(lambda x: x['offset'] != (-1, -1), checking_result))
        if not checking_result:
            return {}

        # 筛选出rank score最大值
        max_rank_score = sorted(checking_result, key=lambda x: x['rank_score'], reverse=True)[0]['rank_score']
        checking_result = list(filter(lambda x: x['rank_score'] == max_rank_score, checking_result))

        # 筛选出match score最大值
        max_match_score = sorted(checking_result, key=lambda x: float(x['match_score']), reverse=True)[0]['match_score']
        checking_result = list(filter(lambda x: x['match_score'] == max_match_score, checking_result))

        # 再按rank排序
        checking_result = sorted(checking_result, key=lambda x: x['rank'], reverse=True)
        # print('address checking:', time.time()-time5)

        # 地址补充输出
        for res in checking_result:
            intersection = res['index']
            high_rank = res['rank']
            address = self.address_complete(intersection[0], high_rank)
            address['last'] = s[res['offset'][1]:]
            return address

        return {}

    def get_index(self, words: list, rank: int):
        """获取词的index"""
        retrieval_model = self.retrieval_model[self.num2rank[rank]]
        indexes = {}
        for word in words:
            retrieval_result = retrieval_model.run(word)
            indexes[word] = retrieval_result
        return indexes

    def address_rank(self, address_segment, address_ranging):
        """地址排列"""
        for item in address_segment:
            item['rank'] = self.rank2num[item['rank']]
            if not address_ranging:
                address_ranging.append([item])
                continue
            for item1 in address_ranging:
                last_ranging = item1[-1]
                if 0 <= (item['offset'][0] - last_ranging['offset'][1]) <= 5 and last_ranging['rank'] < item['rank']:
                    address = copy.copy(item1)
                    address.append(item)
                    address_ranging.append(address)
                elif [item] != address_ranging[-1]:
                    address_ranging.append([item])
        return address_ranging

    @classmethod
    def address_checking(cls, address_result: list, match_address: list, rank, offset):
        """地址校验"""
        if not address_result:
            for item in match_address:
                add = {'index': item['indexes'], 'match_score': 1, 'rank_score': 1, 'rank': rank}
                if rank <= 3:
                    add['offset'] = offset
                else:
                    add['offset'] = (-1, -1)
                address_result.append(add)
            return address_result

        address_res = []
        for address in address_result:
            index = address['index']
            match_score = address['match_score']
            rank_score = address['rank_score']
            last_rank = address['rank']
            for item in match_address:
                match_index = item['indexes']
                section = list(set(index).intersection(set(match_index)))
                if not section:
                    continue

                rank_score_new = rank_score + 1 - (rank - last_rank - 1) / 5
                match_score = match_score * item['score']
                add = {'index': section, 'match_score': match_score, 'rank_score': rank_score_new, 'rank': rank}
                if rank <= 3:
                    add['offset'] = offset
                else:
                    add['offset'] = address['offset']
                address_res.append(add)

        return address_res

    def address_complete(self, address_id, rank):
        """地址补全"""
        line = self.address.iloc[int(address_id)]
        output = {'province': '', 'city': '', 'county': '', 'town': '', 'village': ''}
        keys = list(output.keys())[:rank]
        for key in keys:
            output[key] = line[key]
        return output

    def address_correct(self, data):
        """地址纠错"""
        pass
