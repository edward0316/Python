#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

'''
问题：
1、 print('1. Hubei')
    print('2. Henan')
    print('3. Shandong')
    print('q. Quit')
    类似这样的东西完全可以通过循环里输出，并且可以用一个单独的函数来处理
    （不知道你们学了函数没有，没学也可以事先了解）
2、可以考虑使用字典代替过多的if，else的判断
3、str(input('Please input the index: '))这是啥意思，难道input返回的不是字符串类型的？
4、first = 1
    second = 1
    这两参数只会出现两个值，可以使用布尔类型的，节省资源，效率更高
第二个作业相对第一个作业来说，问题少一点，而且都不是啥大问题，多级菜单的关键点对了，加油！！
'''
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
