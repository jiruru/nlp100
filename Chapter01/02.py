# -*- coding: utf-8 -*-

str1 = 'パトカー'
str2 = 'タクシー'

str3 = "".join([i + j for i, j in zip(str1, str2)])
print(str3)
