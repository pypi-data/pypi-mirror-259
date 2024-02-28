import unittest

from m_mock.m_random import m_name
from m_mock.test_case.common_utils import execute


class TestName(unittest.TestCase):
    def test_name(self):
        execute("""@clast()""")
        execute("""@cfirst()""")
        execute("""@cname()""")
        execute("""@cname(3)""")
        execute("""@last()""")
        execute("""@first()""")
        execute("""@name()""")
        execute("""@name(True)""")
        print(m_name.cfirst())
        print(m_name.clast())
        print(m_name.cname())
        print(m_name.first())
        print(m_name.last())
        print(m_name.name())
        print(m_name.name(True))

    def test_name2(self):
        for i in range(1000):
            i = m_name.cname()
            assert not '\n' in i
            print(i)
