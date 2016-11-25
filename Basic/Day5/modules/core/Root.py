#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import conf.DisplayMenu, conf.Log
import modules.CheckPassword, modules.AtmFunction, modules.RootFunction

while True:
    username = input("Please input the username: ")
    password = input("Please input the password: ")
    temp = modules.CheckPassword.check_password(username, password)
    if temp == 2:
        print("Wrong password or username!")
        continue
    elif temp == 1:
        print("Your account has been frozen")
        continue
    else:
        temp2 = modules.CheckPassword.check_root(username)
        if temp2 == 0:
            print("Welcome %s" % username)
        else:
            print("This account is not a root account.")
            continue
    while True:
        rootMenu = conf.DisplayMenu.dispaly_root()
        try:
            index = int(input('Please input the index: '))
            selection = rootMenu[index]
        except (IndexError,ValueError):
            print("Pleas input the correct index.")
            continue
        if selection == "Add Account":
            modules.RootFunction.add_account(username)
        elif selection == "Change Account Limit":
            modules.RootFunction.change_account_limit(username)
        elif selection == "Froze Account":
            modules.RootFunction.froze_account(username)