# -*- coding: utf-8 -*-
import json


if __name__ == '__main__':
    w = open('./jawiki-country.txt', 'w')
    with open('./jawiki-country.json', 'r') as f:
        for line in f.readlines():
            uk = json.loads(line)
            if uk['title'] == 'イギリス':
                w.write(uk['text'])
