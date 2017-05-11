# -*- coding: utf-8 -*-


if __name__ == '__main__':
    with open('./jawiki-country.txt', 'r') as f:
        for sec in f.readlines():
            count = 0
            if sec[0] == '=':
                for i in range(len(sec)):
                    if sec[i] == '=':
                        count += 1
                    else:
                        print(str(count) + ':' + sec.replace('=', ''))
                        break
