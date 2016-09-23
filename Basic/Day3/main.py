#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

MENU = ['Display ha record', 'Add ha record', 'Delete ha record', 'Quit']




def display(text):
    show = []
    target = 'backend %s' % text
    with open('data.txt', 'r') as file:
        temp = False
        for line in file:
            if not temp and line.strip() != target:
                continue
            if not temp and line.strip() == target:
                temp = True
                continue
            if temp and not line.startswith('backend'):
                show.append(line.strip())
            if temp and line.startswith('backend'):
                break
    return(show)

def add():
    text = input('Please input your order as dic: ')
    dic = eval(text)
    temp = False
    temp2 = False
    backend = dic['backend']
    target = 'backend %s' % backend
    record = 'server: %s weight: %d maxconn: %d' % (dic['record']['server'],
                                                    dic['record']['weight'],
                                                    dic['record']['maxconn'], )
    show = display(backend)
    if not show:
        with open('data.txt', 'r') as f1, open('data_new.txt', 'w') as f2:
            for line in f1:
                f2.write(line)
            f2.write('\nbackend %s\n' % backend)
            f2.write('        %s' % record)
    else:
        with open('data.txt', 'r') as f1, open('data_new.txt', 'w') as f2:
            for line in f1:
                if not temp and line.strip() != target:
                    f2.write(line)
                    continue
                if not temp and line.strip() == target:
                    f2.write(line)
                    temp = True
                    continue
                if temp and not line.startswith('backend'):
                    if line.strip() == record:
                        f2.write(line)
                        temp2 = True
                        continue
                    else:
                        f2.write(line)
                        continue
                if temp and line.startswith('backend'):
                    if temp2:
                        f2.write(line)
                    else:
                        f2.write('        %s\n' % record)
                        f2.write(line)





def delete():
    pass

def main():
    while True:
        print('Welcome to use the system.'.center(40, '-'))
        for item in MENU:
            print(MENU.index(item),item)
        select = input('Please input the index: ')
        try:
            int(select)
        except:
            print('Please input a integer.')
        else:
            if select == '0':
                text = input('Please input backend: ')
                show = display(text)
                for item in show:
                    print(item)
            elif select == '1':
                add()
            elif select == '2':
                pass
            elif select == '3':
                break

main()

