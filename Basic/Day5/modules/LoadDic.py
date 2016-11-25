#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import json

def user_dic():
    try:
        f = open("..\\db\\User", "r")
    except:
        print("File does not exist.")
        exit()
    userDic = json.load(f)
    f.close()
    return userDic

def shopping_menu_dic():
    try:
        f = open("..\\db\\ShoppingMenu", "r")
    except:
        print("File does not exist.")
        exit()
    shoppingMenu = json.load(f)
    f.close()
    return shoppingMenu

def atm_menu_dic():
    try:
        f = open("..\\db\\atmMenu", "r")
    except:
        print("File does not exist.")
        exit()
    atmMenu = json.load(f)
    f.close()
    return atmMenu