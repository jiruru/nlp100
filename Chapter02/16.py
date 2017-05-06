# -*- coding: utf-8 -*-


def split(f, num):
    for i in range(1, len(f)+1):
        print(f[i-1], end='')
        if i == len(f):
            break
        if (i % int(num)) == 0:
            print('')


if __name__ == '__main__':
    f = open('./hightemp.txt').readlines()
    num = input()
    split(f, num)
