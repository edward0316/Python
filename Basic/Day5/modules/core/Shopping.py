#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import conf.DisplayMenu, conf.Log
import modules.CheckPassword, modules.Cart
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
    cart = []
    while True:
        shoppingMenu = conf.DisplayMenu.display_shopping()
        try:
            index = int(input('Please input the index: '))
            selection = shoppingMenu[index]
        except (IndexError,ValueError):
            print("Pleas input the correct index.")
            continue
        if selection == "Check out":
            temp = modules.Cart.purchase(username, cart)
            if temp == False:
                continue
            else:
                break
        elif selection == "Check purchase cart":
            modules.Cart.check_cart(cart)
        elif selection == "Delete item in cart":
            modules.Cart.check_cart(cart)
            cart = modules.Cart.delete(cart)
        else:
            cart.append(selection)
    conf.Log.shopping_log(username, cart)



