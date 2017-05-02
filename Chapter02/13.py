# -*- coding: utf-8 -*-
import re

f1 = open('./col1.txt').readlines()
f2 = open('./col2.txt').readlines()
f3 = open('./col3.txt', 'w')


for i in range(len(open('./col1.txt').readlines())):
    f3.write(str(re.sub(r'\n', '', f1[i])) + '\t' + str(f2[i]))
