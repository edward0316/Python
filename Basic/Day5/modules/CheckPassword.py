#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import json

def check_password(username, password):
    try:
        f = open("..\\db\\User","r")
    except:
        print("File does not exist.")
        exit()
    dic = json.load(f)
    f.close()
    if username in dic.keys():
        if password == dic[username][0]:
            if dic[username][3] == 0:
                return 0
            else:
                return 1 #frozen
        else:
            return 2   #Wrong password
    else:
        return 2   # Username does not exist

def check_root(username):
    try:
        f = open("..\\db\\User","r")
    except:
        print("File does not exist.")
        exit()
    dic = json.load(f)
    f.close()
    if dic[username][4] == 0:
        return 0
    else:
        return 1
#check_password("asd","1234")
