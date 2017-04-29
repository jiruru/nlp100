# -*- coding: utf-8 -*-

def n_gram(str):
    str1 = str.split()
    str2 = str.replace(" ", "")

    print("Words:bigram")
    for i in range(len(str1)):
        if(len(str1)-1 != i):
            print(str1[i], "-", str1[i+1])

    print("Char:bigram")
    for i in range(len(str2)):
        if(len(str2)-1 != i):
            print(str2[i], "-", str2[i+1])

    return None

if __name__ == '__main__':
    str = "I am an NLPer"
    n_gram(str)
