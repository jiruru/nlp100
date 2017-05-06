# -*- coding: utf-8 -*-


if __name__ == '__main__':
    f = open('./hightemp.txt').readlines()
    char = []
    for i in range(len(f)):
        if f[i][0] not in char:
            char.append(f[i][0])
    print(char)
