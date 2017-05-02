# -*- coding: utf-8 -*-

f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')

for i in open("./hightemp.txt"):
    f1.write(str(i.split('\t')[0]+"\n"))
    f2.write(str(i.split('\t')[1]+"\n"))
