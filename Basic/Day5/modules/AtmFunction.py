#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import json
import conf.Log
import modules.LoadDic as LoadDic


def withdraw(username):
    userDic = LoadDic.user_dic()
    triger = 1
    while triger == 1:
        print("There will be a 5% surcharge for the withdraw.".center(40,"-"))
        try:
            withdrawAmount = float(input("Please input the amount, input 0 for exit: "))
        except TypeError:
            print("Please input a number")
            continue
        if withdrawAmount == 0:
            triger = 0
        elif withdrawAmount * 1.05 <= userDic[username][1]:
            userDic[username][1] = userDic[username][1] - withdrawAmount
            print("Your current balance is %d" % userDic[username][1])
            json.dump(userDic, open("..\\db\\User", "w"))
            conf.Log.withdraw_log(username, withdrawAmount)

            triger = 0
        else:
            print("Your current balance is %d which is not enough." % userDic[username][1])


def transfer(username):
    triger = 1
    triger2 = 1
    userDic = LoadDic.user_dic()
    while triger == 1:
        target = input("Please input the target user, leave blank to give up: ")
        if target in userDic.keys():
            while triger2 == 1:
                try:
                    amount = float(input("Please input the transfer amount, input 0 or leave blank to give up: "))
                except (ValueError, TypeError):
                    print("Please input a number!")
                    continue
                if amount == 0:
                    triger2 = 0
                    continue
                elif amount <= userDic[username][1]:
                    userDic[username][1] = userDic[username][1] - amount
                    userDic[target][1] = userDic[target][1] + amount
                    print("The transfer has been done.")
                    json.dump(userDic,open("..\\db\\User", "w"))
                    conf.Log.transfer_log(username, target, amount)
                    triger2 = 0
                    triger = 0
                else:
                    print("Your balance is not enough.")
        elif target == "":
            triger = 0
            continue
        else:
            print("Plese input an correct username!".center(30,"*"))
            continue


def bank_statement(username):
    file = "..\\log\\%s.log" % username
    try:
        f = open(file, "r")
    except FileNotFoundError:
        print("The history does not exist.")
        exit()
    statement = f.read()
    print(statement)

def pay_back(username):
    userDic = LoadDic.user_dic()
    oweMoney = userDic[username][2] - userDic[username][1]
    triger = 1
    while triger == 1:
        print("You owe %d to the bank currently." % oweMoney)
        try:
            amount = float(input("Please input the money you want to pay back, input 0 to give up: "))
        except (ValueError, TypeError):
            print("Please input the correct number: ")
            continue
        if amount > oweMoney:
            print("You only owe %d to the bank. The system will adjust the amount to %d automatically"
                  % (oweMoney, oweMoney))
            print("You have payed back %d to the bank, and you owe 0 to the bank now." % oweMoney)
            userDic[username][1] = userDic[username][2]
            json.dump(userDic, open("..\\db\\User", "w"))
            conf.Log.pay_back_log(username, oweMoney)
            triger = 0
        else:
            currentOwe = oweMoney - amount
            print("You have payed back %d to the bank, and you owe %d to the bank now." % (oweMoney,currentOwe))
            userDic[username][1] = userDic[username][1] + amount
            json.dump(userDic, open("..\\db\\User", "w"))
            conf.Log.pay_back_log(username, amount)
            triger = 0