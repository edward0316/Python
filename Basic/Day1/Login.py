#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
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




