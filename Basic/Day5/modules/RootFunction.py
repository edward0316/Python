#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import json
import modules.LoadDic as LoadDic
import conf.Log as Log

def add_account(admin):
    while True:
        print("Leave the account name empty to give up.")
        accountName = input("Please input the account name: ")
        if accountName == "":
            break
        accountPassword = input("Please input the account password: ")
        userDic = LoadDic.user_dic()
        userDic[accountName] = [accountPassword, 15000, 15000, 0, 1]
        json.dump(userDic, open("..\\db\\User", "w"))
        Log.add_account(admin, accountName)
        break


def change_account_limit(admin):
    while True:
        print("Leave the account name empty to give up.")
        accountName = input("Please input the account name: ")
        if accountName == "":
            break
        while True:
            try:
                amountLimit = float(input("Please input the new amount limit: "))
            except TypeError:
                print("Please input the correct number!")
            userDic = LoadDic.user_dic()
            userDic[accountName][2] = amountLimit
            json.dump(userDic, open("..\\db\\User", "w"))
            Log.change_account_limit(admin, accountName, amountLimit)
            break
        break


def froze_account(admin):
    while True:
        print("Leave the account name empty to give up.")
        accountName = input("Please input the account name: ")
        if accountName == "":
            break
        while True:
            decison = input("Are you sure to forze this account? Y or N: ")
            if decison == "Y":
                userDic = LoadDic.user_dic()
                userDic[accountName][3] = 1
                json.dump(userDic, open("..\\db\\User", "w"))
                Log.froze_account(admin, accountName)
                break
            elif decison == "N":
                print("Give up")
                break
            else:
                print("Please input Y or N, it is case sensitive.")
        break

