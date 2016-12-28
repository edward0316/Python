#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import os


def identifyAdmin(username, password, account_type):
    from xml.etree import ElementTree as ET
    if os.path.exists(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", account_type, username)):
        tree = ET.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", account_type, username, "profile.xml"))
        root = tree.getroot()
        for i in root.iter("password"):
            passwd = i.text
        if password == passwd:
            return 0
        else:
            print("Username or Password is incorrect.")
            return 1
    else:
        print("Username or Password is incorrect.")
        return 1

def identifyOther(username, password, account_type):
    import pickle
    try:
        file_name = username + ".pkl"
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", account_type, file_name), "rb")
        obj = pickle.load(file)
        if obj.password == password:
            return [0, obj]
        else:
            print("Username or Password is not correct. Please try again.")
            return [1]
    except FileNotFoundError:
        print("Username or Password is not correct. Please try again.")
        return  [1]