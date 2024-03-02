# -*- coding:utf-8 -*-
"""
@Time        : 2023/11/3
@File        : hypothesis_data.py
@Author      : lyz
@version     : python 3
@Description :
"""
from hypothesis import given,settings
from hypothesis import strategies as st

# ASCII 数字字符集: '1','2'
char_num = st.characters(min_codepoint=48, max_codepoint=57)
# ASCII 字母字符集：'a','A'
alphabet = st.characters(min_codepoint=65, max_codepoint=90) | st.characters(min_codepoint=97, max_codepoint=122)
# ASCII 特殊字符集：'?','*'
special = (st.characters(min_codepoint=33, max_codepoint=47) | st.characters(min_codepoint=58, max_codepoint=64) |
          st.characters(min_codepoint=91, max_codepoint=96) | st.characters(min_codepoint=123, max_codepoint=126))
# ASCII 乱码集：
garbled = st.characters(min_codepoint=0, max_codepoint=32)
garbled127 = st.characters(min_codepoint=127,max_codepoint=127)

# 半角符号字符集：
half_ascll = st.characters(min_codepoint=33, max_codepoint=126)
# 全角符号字符集：
all_ascll = st.characters(min_codepoint=0xFF00, max_codepoint=0xFFEF)
# Emoji 字符集:
emoji = (st.characters(min_codepoint=0x1F600, max_codepoint=0x1F64F) |
         st.characters(min_codepoint=0x1F300, max_codepoint=0x1F5FF) |
         st.characters(min_codepoint=0x1F680, max_codepoint=0x1F6FF))
# 货币符号字符集
symbol_money = st.characters(min_codepoint=0x20AC, max_codepoint=0x20CF) | st.characters(min_codepoint=0x20B0, max_codepoint=0x20BD)
# 数学符号字符集
symbol_math = st.characters(min_codepoint=0x2200, max_codepoint=0x22FF)
# 中文字符集：'刘','国'
chinese = st.characters(min_codepoint=0x4E00, max_codepoint=0x9FA5)
# unicode字符集
unicode = st.characters(min_codepoint=0, max_codepoint=0x10FFFF)



@given(a=unicode)
def func(a):
    print(a)

if __name__ == '__main__':
    func()
