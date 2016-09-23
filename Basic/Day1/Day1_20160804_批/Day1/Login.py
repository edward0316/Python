#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
'''
问题：
1、有些东西最好不要写死比如用来保存用户信息的文件名“user.txt”最好写到一个配置文件里，
   如果只是脚本级别的小东西也要以常量的形式在上方定义，这样方便统一修改，向你的代码里多次
   引用了这文件名，如果要修改就会出现漏掉的情况
2、在对文件进行操作前，尤其是读，一定要判断文件是否存在（切记），如果文件不存在，则可以友好的报错，
   否则执行到会出现非常不友好的异常
3、 for i in range(len(text)):
        user, password,tag, count = text[i].split(' ')
        users.append(user)
        passwords.append(password)
        tags.append(int(tag.strip()))
        counts.append(int(count.strip()))
    以上的代码完全是多余的完全一边循环一边判断一边写回到文件
4、for i in range(len(text)):
        text_final = users[i] + ' ' + passwords[i] + ' ' + str(tags[i]) + ' ' + str(counts[i]) + '\n'
        file = open('user.txt', 'a')
        file.writelines(text_final)
        file.close()
    这段代码出现了两次，为什么不直接写成一个函数呢
5、text_final = users[i] + ' ' + passwords[i] + ' ' + str(tags[i]) + ' ' + str(counts[i]) + '\n'
   这种形式的字符串拼接非常低效和浪费资源，（因为无形中python解释器要另外开辟一块儿空间来保存相加后的结果，
   有多少次相加就开辟多少次）。另外相加的对象必须都是字符串，如果有数字还得做转换
   如果程序达到一定规模是非常慢的
   正确的字符串拼接的话有占位符、format方法，join方法


'''
while True:
    #loading the file
    users = []
    passwords = []
    tags = []
    counts = []
    file = open('user.txt')
    text = file.readlines()
    file.close()
    for i in range(len(text)):
        user, password,tag, count = text[i].split(' ')
        users.append(user)
        passwords.append(password)
        tags.append(int(tag.strip()))
        counts.append(int(count.strip()))
    input_user = input('Please input your username: ')
    input_password = input('Please input your password: ')
    if input_user in users:
        if tags[users.index(input_user)] == 0:
            if input_password == passwords[users.index(input_user)]:
                print('Welcome %s'% input_user)
                break
            else:
                print('Sorry, you get the wrong username or password, please try again.')
                if counts[users.index(input_user)] > 1:
                    counts[users.index(input_user)] -= 1
                    print('You have %d chances to try' % counts[users.index(input_user)])
                    #Clear the file
                    file = open('user.txt', 'w')
                    file.close()
                    #Adding modified lines into the file
                    for i in range(len(text)):
                        text_final = users[i] + ' ' + passwords[i] + ' ' + str(tags[i]) + ' ' + str(counts[i]) + '\n'
                        file = open('user.txt', 'a')
                        file.writelines(text_final)
                        file.close()
                else:
                    tags[users.index(input_user)] = 1
                    print('Your account is locked due to more than 3 times login attempts.')
                    file = open('user.txt', 'w')
                    file.close()
                    for i in range(len(text)):
                        text_final = users[i] + ' ' + passwords[i] + ' ' + str(tags[i]) + ' ' + str(counts[i]) + '\n'
                        file = open('user.txt', 'a')
                        file.writelines(text_final)
                        file.close()
                    break
        else:
            print('Your account is locked due to more than 3 times login attempts.')
            break
    else:
        print('Sorry, you get the wrong username or password, please try again.')




