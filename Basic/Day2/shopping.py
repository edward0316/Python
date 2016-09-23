#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import shopping_list
import datetime

user = {}#load the user file into the dict
all_history = {}
def clear_file(file):
    try:
        f = open(file, 'w')
        f.close()
    except:
        print('File is not exist.')


def modify_file(file, text):
    try:
        f = open(file, 'a')
        f.writelines(text)
        f.close()
    except:
        print('File is not exist.')

def input_index(n):
    while True:
        temp = input('Please input the index: ')
        if temp == 'q':
            return temp
            break
        elif temp == 'b':
            return temp
            break
        elif temp == 'c':
            return temp
            break
        else:
            try:
                temp = int(temp)
            except:
                print('Please input the right index.')
                continue
            if 0 <= temp < n:
                return temp
                break
            else:
                print('Please input the right index.')

# Load the user information
def read_file(file_name, dic_name):
    try:
        file = open(file_name, 'r')
        text = file.readlines()
        #text = text.replace('\n', '')
        #    print(text)
        for i in range(len(text)):

            text[i] = text[i].replace('\n', '')
            text[i] = text[i].split(' ')
           # text[i][4] = text[i][4].replace('\n', '')
            dic_name[text[i][0]] = text[i][1:]
    except:
        print('File is not exist 1')

def check(name):
    for i in all_history[name]:
        print(i)



read_file('user.txt', user)
read_file('history.txt', all_history)
print(user)
print(all_history)
print('Welcome to use the shopping software'.center(40, '-'))
while True:
    username = input('Please input your username: ')
    password = input('Please input your password: ')
    #identify the user, the account will be locked after 3 attempts.
    if username in user:
        count = int(user[username][2])
        tag = user[username][1]
        if tag == '0':
            if password == user[username][0]:
                print('Welcome %s'.center(40, '-') % username)
                break
            else:
                print('Your username or password is wrong.')
                user[username][2] = str(count - 1)
                if user[username][2] == '0':
                    user[username][1] = '1'
                    print('Your account has been locked.')
                clear_file('user.txt')
                for i in user.keys():
                    text_final = '%s %s %s %s %s\n' % (i, user[i][0], user[i][1], user[i][2], user[i][3])
                    modify_file('user.txt', text_final )
        else:
            print('Your account is locked.'.center(40,'*'))
    else:
        print('Wrong password or username.')

balance = int(user[username][3])
print('Your balance is %d' % balance)
first = True
second = True
while first:
    #Topup the wallet.
    money = input('Please topon your balance. input 0 for give up topon: ')
    if money.isdigit():
        balance = balance + int(money)
        print('You current balance is %d' % balance)
        user[username][3] = str(balance)
        clear_file('user.txt')
        for i in user.keys():
            text_final = '%s %s %s %s %s\n' % (i, user[i][0], user[i][1], user[i][2], user[i][3])
            modify_file('user.txt', text_final)
    else:
        print('Please input a integer')
        continue

    main_menu = []
    for i in shopping_list.shopping_list.keys():
        main_menu.append(i)
        print(main_menu.index(i), i)
    print('c Check balance\nq Quit')

    select_first = input_index(len(main_menu))

    if select_first == 'q':
        first = False
        continue
    elif select_first == 'c':
        check(username)
    else:
        while second:
            second_menu = []
            for i in shopping_list.shopping_list[main_menu[select_first]].keys():
                item = [i,shopping_list.shopping_list[main_menu[select_first]][i]]
                second_menu.append(item)
                print(second_menu.index(item), item)
            print('c Check balance\nb Back\nq Quit')
            select_second = input_index(len(second_menu))
            if select_second == 'b':
                break
            elif select_second == 'q':
                first = False
                break
            elif select_second == 'c':
                check(username)
            else:
                if balance >= second_menu[select_second][1]:
                    balance = balance - second_menu[select_second][1]
                    print('Congratulations. The purchase process is successful. Your current balance is %d.'
                          % balance)
                    now = datetime.datetime.now().strftime('%c').replace(' ','.')
                    purchase = '%s|%s|%s ' % (now, second_menu[select_second][0], second_menu[select_second][1])
                    all_history[username].append(purchase)
                    clear_file('history.txt')
                    for i in all_history.keys():
                        text = ' '.join(all_history[i])
                        text_final = '%s %s\n' % (i, text)
                        modify_file('history.txt', text_final)
                else:
                    print('You balance is %d. You cannot afford this item.' % balance)




