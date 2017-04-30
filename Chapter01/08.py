# -*- coding: utf-8 -*-


def chiper(string):
    str = []
    for i in range(len(string)):
        if string[i].islower():
            str.append("".join(chr(219 - ord(string[i]))))
        else:
            str.append("".join(string[i]))
    return str


def rechiper(string):
    str = []
    for i in range(len(string)):
        if string[i].islower():
            str.append("".join(chr(219 - ord(string[i]))))
        else:
            str.append("".join(string[i]))
    return str


if __name__ == '__main__':
    str = input()
    cip1 = chiper(str)
    cip2 = rechiper(cip1)
    print(cip1)
    print(cip2)
