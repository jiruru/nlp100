# -*- coding: utf-8 -*-
import re


def pre_match(r):
    return r.string[:r.start()]


def post_match(r):
    return r.string[r.end():]


if __name__ == '__main__':
    with open('./jawiki-country.txt', 'r') as f:
        for cat in f.readlines():
            if 'Category' in cat:
                r = post_match(re.search(re.escape('[[Category:'), str(cat)))
                print(pre_match(re.search(re.escape(']]'), r)))
