#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import json

def check_cart(item):
    try:
        f = open("..\\db\\ShoppingMenu","r")
    except:
        print("File does not exist!")
        exit()
    itemDic = json.load(f)
    f.close()
    print("Cart list".center(20, "-"))
    for i in item:
        print("%s %d" %(i, itemDic[i]))
    print("".center(20, "-"))


def purchase(username, item):
    try:
        f1 = open("..\\db\\ShoppingMenu","r")
        f2 = open("..\\db\\User", "r")
    except:
        print("File does not exist!")
        exit()
    itemDic = json.load(f1)
    userDic = json.load(f2)
    f1.close()
    f2.close()
    amount = 0
    for i in item:
        amount = amount + itemDic[i]
    if userDic[username][1] >= amount:
        remainMoney = userDic[username][1] - amount
        userDic[username][1] = remainMoney
        json.dump(userDic, open("..\\db\\User", "w"))
    else:
        print("Your current balance is %d which is not enough." % userDic[username][1])
        return False

def delete(item):
    target = input("Please input the item name to delete, or input exit for giving up: ")
    if target in item:
        item.remove(target)
        return item
    elif target == "exit":
        exit()
    else:
        print("Please input the correct word.")

