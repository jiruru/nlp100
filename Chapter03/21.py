# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open('./jawiki-country.txt', 'r') as f:
        for cat in f.readlines():
            if 'Category' in cat:
                print(cat)
