#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
first = 1
second = 1

while first == 1:
    print('1. Hubei')
    print('2. Henan')
    print('3. Shandong')
    print('q. Quit')
    prov = str(input('Please input the index: '))
    if prov == '1':
        while second == 1:
            print('1. Wuhan')
            print('2. Yichang')
            print('3. Huangshi')
            print('b. Back')
            print('q. Quit')
            city = str(input('Please input the index: '))
            if city == '1':
                while True:
                    print('1. Luoshi Road')
                    print('2. Xiongchu Road')
                    print('3. Renmin Road')
                    print('b. Back')
                    print('q. Quit')
                    road = str(input('Please input the index: '))
                    if road == 'b':
                        break
                    elif road == 'q':
                        first = 0
                        second = 0
                        break
                    else:
                        print('Thank you for using the system!!')
                        first = 0
                        second = 0
                        break
            elif city == '2':
                pass
            elif city == '3':
                pass
            elif city == 'b':
                break
            elif city == 'q':
                first = 0
                break
    elif prov == '2':
        pass
    elif prov == '3':
        pass
    elif prov == 'q':
        break
