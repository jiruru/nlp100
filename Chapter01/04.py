# -*- coding: utf-8 -*-
from collections import OrderedDict

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()

i = 0
Element_dic = OrderedDict()

for num in (str):
    if i in (0, 4, 5, 6, 7, 8, 14, 15, 18):
        Element_dic[str[i][:1]] = i+1
    else:
        Element_dic[str[i][:2]] = i+1
    i = i + 1

for key, value in Element_dic.items():
    print(key, value)
