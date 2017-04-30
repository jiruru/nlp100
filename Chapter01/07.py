# -*- coding: utf-8 -*-


def ret_CharString(time, string, temp):
    CharSt = str(time)+"時の"+string+"は"+str(temp)
    return CharSt


if __name__ == '__main__':

    print(ret_CharString(12, "気温", 22.4))
