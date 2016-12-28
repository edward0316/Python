#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import os
import conf.menu as menu


while True:
    print(menu.first_menu)
    list = ["1","2","3","4"]
    select = input("Please input the index: ").strip()
    if select not in list:
        print("Please input the correct index, 1, 2 or 3.")
        continue
    else:
        pass
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    import modules.identify
    #admin
    if select == "1":
        result = modules.identify.identifyAdmin(username,password, "admin")
        if result == 0:
            import modules.admin
            while True:
                print(menu.admin_menu)
                select = input("Please input the index: ")
                if select == "1": #Add teacher account
                    modules.admin.teacher()
                elif select == "2": # Add student account
                    modules.admin.student()
                elif select == "3": # Add units
                    modules.admin.unit()
                elif select == "4": #show unit status
                    modules.admin.showUnitStatus()
                elif select == "5":# Log out
                    break
                else:
                    print("Please input the correct index: ")
        else:
            continue
    #student
    elif select == "2":
        result = modules.identify.identifyOther(username, password, "student")
        if result[0] == 0:
            student = result[1]
            while True:
                print(menu.student_menu_1)
                select = input("Please input the index: ")
                if select == "1": #Change Password
                    student.changPassword()
                elif select == "2": # Show All Units
                    student.showAllUnits()
                elif select == "3": # Enroll a unit
                    student.enrollUnit()
                elif select == "4": # Show all enrolled units
                    student.showStatus()
                elif select == "5": # Deposit tuition
                    student.depositTuition()
                elif select == "6": # Log Out
                    break
                else:
                    print("Please input the correct index: ")
        else:
            continue
    #teacher
    elif select == "3":
        result = modules.identify.identifyOther(username, password, "teacher")
        if result[0] == 0:
            teacher = result[1]
            while True:
                print(menu.teacher_menu)
                select = input("Please input the index: ")
                if select == "1":  # Change Password
                    teacher.register()
                elif select == "2":  # Show All Units
                    teacher.showStatus()
                elif select == "3":
                    break
                else:
                    print("Please input the correct index.")
    #Quit
    elif select == "4":
        break

