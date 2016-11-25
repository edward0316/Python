#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import conf.DisplayMenu, conf.Log
import modules.CheckPassword, modules.AtmFunction
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
        print("Welcome %s" % username)
        pass
    while True:

        atmMenu = conf.DisplayMenu.dispaly_atm()
        try:
            index = input('Please input the index: ')
            selection = atmMenu[index]
        except (IndexError,ValueError):
            print("Pleas input the correct index.")
            continue
        if selection == "Withdraw":#Withdraw function
            modules.AtmFunction.withdraw(username)
        elif selection == "Transfer":#Transfer function
            modules.AtmFunction.transfer(username)
        elif selection == "Bank Statement":#Bank statement function
            modules.AtmFunction.bank_statement(username)
        elif selection == "Pay back":#Pay back function
            modules.AtmFunction.pay_back(username)
   # conf.Log.shopping_log(username, cart)
