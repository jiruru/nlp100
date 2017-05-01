# -*- coding: utf-8 -*-
import random


def shuffle(word):
    result = "".join(random.sample(word, len(word)))
    return result


def typoglycemia(string):
    if len(string) < 5:
        return string
    else:
        result = string[0] + shuffle(string[1:-1]) + string[-1]

    return reslut


if __name__ == '__main__':
    string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split()
    result = []

    for i in range(len(string)):
        result.append("".join(typoglycemia(string[i])))

    print(result)
