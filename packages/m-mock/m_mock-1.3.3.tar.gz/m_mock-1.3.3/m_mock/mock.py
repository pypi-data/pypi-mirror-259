import re

from m_mock import m_random


class MockM:

    def mock(self, mock_str):
        keyword = self.get_mocker_key(mock_str)
        args = self.get_mocker_params_to_tuple(mock_str)
        if keyword == 'date':
            return m_random.m_date.date(*args)
        elif keyword == 'datetime':
            return m_random.m_date.datetime(*args)
        elif keyword == 'time':
            return m_random.m_date.time(*args)
        elif keyword == 'now':
            return m_random.m_date.now(*args)
        elif keyword == 'float':
            return m_random.m_float.float(*args)
        elif keyword == 'natural':
            return m_random.m_natural.natural(*args)
        elif keyword == 'integer':
            return m_random.m_integer.integer(*args)
        elif keyword == 'boolean':
            return m_random.m_boolean.boolean(*args)
        elif keyword == 'character':
            return m_random.m_character.character(*args)
        elif keyword == 'string':
            return m_random.m_string.string(*args)
        elif keyword == 'pick':
            return m_random.m_helper.pick(*args)
        elif keyword == 'cfirst':
            return m_random.m_name.cfirst(*args)
        elif keyword == 'clast':
            return m_random.m_name.clast(*args)
        elif keyword == 'cname':
            return m_random.m_name.cname(*args)
        elif keyword == 'first':
            return m_random.m_name.first(*args)
        elif keyword == 'last':
            return m_random.m_name.last(*args)
        elif keyword == 'name':
            return m_random.m_name.name(*args)
        else:
            return mock_str

    @classmethod
    def get_mocker_key(cls, mock_str):
        if not mock_str.startswith('@'):
            raise m_random.MockPyExpressionException()
        if not mock_str.endswith(')'):
            # 非)结尾说明是@date,则直接返回属性名
            return mock_str[1:]
        regular = '(?<=(\\@)).*?(?=(\\())'
        keyword = re.search(regular, mock_str).group(0)
        return keyword

    @classmethod
    def get_mocker_params_to_tuple(cls, mock_params) -> tuple:
        """
        将参数组装为元组，方便后续解包

        :param mock_params: ('%Y.%m.%d %H:%M:%S','+1')
        :return: 元组
        """

        # 正则表达式匹配字符串中括号内的内容
        regular = '[\\(|（].*[\\)|）]$'
        match = re.search(regular, mock_params)
        if match is None:
            return ()
        group = match.group(0)
        if group == '()':
            return ()
        end_val = group[-1:]
        if not end_val.endswith(','):
            group = f'{group[:-1]},)'
        args = eval(group)
        return args


m_mock = MockM()
