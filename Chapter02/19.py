# -*- coding: utf-8 -*-


if __name__ == '__main__':
    f = open('./hightemp.txt').readlines()
    char = {}

    for i in range(len(f)):
        if f[i].split('\t')[0] not in char.keys():
            char[f[i].split('\t')[0]] = 1
        else:
            char[f[i].split('\t')[0]] = 1 + char[f[i].split('\t')[0]]
    for k, v in reversed(sorted(char.items(), key=lambda x:x[1])):
        print(k,v)
