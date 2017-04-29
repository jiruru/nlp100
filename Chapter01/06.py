# -*- coding: utf-8 -*-

#n-gram
def n_gram(str):
    str1 = (len(str)-1)*[0]

    for i in range(len(str)):
        if(len(str)-1 != i):
            str1[i] = (str[i] + str[i+1])

    return str1

if __name__ == '__main__':
    str = "paraparaparadise"
    str1 = "paragraph"
    x = set(n_gram(str))
    y = set(n_gram(str1))

    #union
    sum = x.union(y)
    print(sum)

    #intersection
    intersection = x&y
    print(intersection)

    #set difference
    diff1 = x.difference(y)
    diff2 = y.difference(x)
    print(diff1)
    print(diff2)

    #include
    print("se" in x)
    print("se" in y)
