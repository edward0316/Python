#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import pickle
import os
import modules.role

def teacher():
    while True:
        name = input("Please input the teacher's name: ")
        file_name = name + ".pkl"
        try:
            file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "teacher", file_name), "r")
            file.close()
            print("The username is exist. Please try another name")
            continue
        except FileNotFoundError:
            password = input("Please input the teacher's password: ")
            age = input("Please input the teacher's age: ")
            tutor = modules.role.Teacher(name, password, age)
            file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "teacher", file_name), "wb")
            pickle.dump(tutor, file)
            file.close()
            break

def student():
    while True:
        name = input("Please input the student's name: ")
        file_name = name + ".pkl"
        try:
            file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "student", file_name), "r")
            file.close()
            print("The username is exist. Please try another name")
            continue
        except FileNotFoundError:
            password = input("Please input the student's password: ")
            age = input("Please input the student's age: ")
            stu = modules.role.Student(name, password, age)
            file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "student", file_name), "wb")
            pickle.dump(stu, file)
            file.close()
            break

def unit():
    while True:
        name = input("Please input the unit's name: ")
        file_name = name + ".pkl"
        try:
            file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "units", file_name), "r")
            file.close()
            print("The username is exist. Please try another name")
            continue
        except FileNotFoundError:
            tuition = input("Please input the tution: ")
            salary = input("Please input the payment for teacher.")
            uni = modules.role.Unit(name, tuition, salary)
            file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "units", file_name), "wb")
            pickle.dump(uni, file)
            file.close()
            break

def showUnitStatus():
    import re
    while True:
        list = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "units"))
        list.remove("__init__.py")
        new_list = []
        for i in list:
            t = re.split("\.pkl", i)
            new_list.append(t[0])
        for i in new_list:
            print("%s. %s" % (new_list.index(i), i))
        select = input("Please input the index: ")
        try:
            unit = list[int(select)]
            file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "units", unit), "rb")
            unit_obj = pickle.load(file)
            file.close()
            print("%s is the teacher for %s" % (unit_obj.teacher, unit_obj.name))
            print("Student list: ")
            for i in unit_obj.student:
                print(i)
            break
        except (IndexError, NameError, ValueError, FileNotFoundError):
            print("Please input the right index. Try again")