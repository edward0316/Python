#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import os
import pickle

class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

class Teacher:
    def __init__(self, name, password, age, asset=0):
        self.name = name
        self.age = age
        self.asset = asset
        self.password = password
        self.unit = []

    def register(self):
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
                self.asset = self.asset + int(unit_obj.salary)
                self.unit.append(new_list[int(select)])
                file_name = self.name + ".pkl"
                file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "teacher", file_name), "wb")
                pickle.dump(self, file)
                print("You have register the unit %s successfully. Your salary is increased %d dollers." % \
                      (new_list[int(select)], self.asset))
                unit_obj.teacherRegister(self.name)
                break
            except (IndexError, NameError, ValueError, FileNotFoundError):
                print("Please input the right index. Try again")

    def showStatus(self):
        print("Your current salary is %d" % self.asset)
        print("You have register the following units: ")
        for i in self.unit:
            print(i)



class Student:
    def __init__(self, name, password, age, asset=0):
        self.name = name
        self.password = password
        self.age = age
        self.asset = asset
        self.unit = []

    def changPassword(self):
        old_password = input("Please input the old password: ")
        if old_password == self.password:
            while True:
                new_password1 = input("Please input the new password: ")
                new_password2 = input("Please input the new password again: ")
                if new_password1 == new_password2:
                    self.password = new_password2
                    print("Password has been changed!")
                    try:
                        file_name = self.name + ".pkl"
                        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "student", \
                                                 file_name), "wb")
                        pickle.dump(self, file)
                        file.close()
                    except FileNotFoundError:
                        pass
                    break
                else:
                    print("The two passwords do not match, please try again.")

    def showAllUnits(self):
        import re
        list = os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "units"))
        list.remove("__init__.py")
        new_list = []
        for i in list:
            t = re.split("\.pkl", i)
            new_list.append(t[0])
        for i in new_list:
            print("%s. %s" % (new_list.index(i), i))

    def enrollUnit(self):
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
                self.asset = self.asset - int(unit_obj.tuition)
                self.unit.append(new_list[int(select)])
                file_name = self.name + ".pkl"
                file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "student", file_name), "wb")
                pickle.dump(self, file)
                print("You have enrolled the unit %s successfully. You have left %d dollers." % \
                      (new_list[int(select)], self.asset))
                unit_obj.studentEnroll(self.name)
                break
            except (IndexError, NameError, ValueError, FileNotFoundError):
                print("Please input the right index. Try again")


    def showStatus(self):
        print("Your current asset is %d" % self.asset)
        print("Your have enrolled the following units: ")
        for i in self.unit:
            print(i)

    def depositTuition(self):
        while True:
            try:
                deposit = int(input("Please input the money: "))
            except (ValueError):
                print("Please input the right number.")
                continue
            self.asset = self.asset + deposit
            file_name = self.name + ".pkl"
            file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "student", file_name), "wb")
            pickle.dump(self, file)
            file.close()
            print("Your asset is %d now." % self.asset)
            break



class Unit:
    def __init__(self, name, tuition, salary):
        self.name = name
        self.tuition = tuition
        self.salary = salary
        self.student = []
        self.teacher = ""

    def studentEnroll(self, student):
        self.student.append(student)
        file_name = self.name + ".pkl"
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "units", file_name), "wb")
        pickle.dump(self, file)
        file.close()

    def teacherRegister(self, teacher):
        self.teacher = teacher
        file_name = self.name + ".pkl"
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "units", file_name), "wb")
        pickle.dump(self, file)
        file.close()