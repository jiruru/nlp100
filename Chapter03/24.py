# -*- coding: utf-8 -*-
import re


f = open('./jawiki-country.txt', 'r').readlines()

for fi in f:
    fitype = re.search(u'\[\[(File|ファイル):(.*?)\|.*?\]\]', fi)
    if fitype:
        print(fitype.group(2))
