# -*- coding: utf-8 -*-


if __name__ == '__main__':
    f = open('./hightemp.txt').readlines()
    for i in reversed(f):
        print(i, end='')
