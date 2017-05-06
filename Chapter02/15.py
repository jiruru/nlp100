# -*- coding: utf-8 -*-


def outhead(f, num):
    for i in range(len(f)):
        if i == int(num):
            break
        print(f[-i-1], end='')


if __name__ == '__main__':
    f = open('./hightemp.txt').readlines()
    num = input()

    outhead(f, num)
