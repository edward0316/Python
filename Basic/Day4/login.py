#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward


MENU = {"1": "Login", "2": "Register", "3": "Quit"}
MORMAL_USER = {"1": "Change Password", "2": "Brows Information", "3": "Logout"}
ROOT_USER = {"1": "Change Password",
             "2": "Brows This Account Information",
             "3": "Brows The Information of All Normal Users",
             "4": "Adding, Deleting, Modifying Normal User",
             "5": "Logout"
             }

ROOT_USER_SECOND = {
    "1": "Adding User",
    "2": "Modifying User",
    "3": "Deleting user",
    "4": "Searching",
    "5": "Back"
}





# display menu in order.
def display_menu(menu):
    index = []
    for i in menu.keys():
        index.append(i)
    index.sort()
    for i in index:
        print(i, menu[i])


def brows_this_user(user, information):
    temp = []
    for i in information[user]:
        temp.append(i)
    s = "Email: %s \nAddress: %s \n" % (temp[2], temp[3])
    print(s)


def brows_other_user(information):
    user = input("Please input the user which you want to check: ")
    if user in information.keys():
        brows_this_user(user, information)
    else:
        print("This user does not exist.")

def outer(func):
    def inner(user, information):
        pssswd = input('Please input your old-password: ')
        if pssswd == str(information[user][0]):
            func(user, information)
        else:
            print('Worng password!')
    return inner


@outer
def change_password(user, information):
    new_password = input("Please input your new password: ")
    information[user][0] = new_password
    with open("user.txt", "w") as file:
        for i in information:
            file.writelines("%s|%s\n" % (i, "|".join(information[i])))
    print('The password has been changed')


def add_modify_delete_user(information):
    while True:
        display_menu(ROOT_USER_SECOND)
        select = input('Please input the index of choice: ')
        if select in ROOT_USER_SECOND.keys():

            #Adding user
            if select == "1":
                username = input('Please input the username: ')
                password = input('Please input the password: ')
                while True:
                    is_root = input('Input 1 for normal user, 0 for root user: ')
                    if is_root == "1" or "0":
                        break
                    else:
                        print('Please input 1 or 0')
                email = input('Please input the email: ')
                address = input('Please input the address: ')
                if username not in information.keys():
                    information[username] = [password, is_root, email, address]
                    with open("user.txt", "w") as file:
                        for i in information:
                            file.writelines("%s|%s\n" % (i, "|".join(information[i])))
                    print('The user has been added successfully!')
                else:
                    print("The user has existed.")

            #Modify user
            elif select == "2":
                username = input("Please input the username: ")
                if username in information.keys():
                    brows_this_user(username, information)
                    password = input('Please input the password: ')
                    while True:
                        is_root = input('Input 1 for normal user, 0 for root user: ')
                        if is_root == "1" or "0":
                            break
                        else:
                            print('Please input 1 or 0')
                    email = input('Please input the email: ')
                    address = input('Please input the address: ')
                    information[username] = [password, is_root, email, address]
                    with open("user.txt", "w") as file:
                        for i in information:
                            file.writelines("%s|%s\n" % (i, "|".join(information[i])))
                    print('The user has been modified successfully!')
                else:
                    print('The user does not exist.')

            #Delete user
            elif select == "3":
                username = input("Please input the username: ")
                if username in information.keys():
                    information.pop(username)
                    print('The user has been deleted successfully!')
                else:
                    print('The user does not exist.')

            #Searching
            elif select == "4":
                tag = 0
                search = input('Please input your search key: ')
                for i in information:
                    s = "%s|%s\n" % (i, "|".join(information[i]))
                    if search in s:
                        print(s)
                        tag = 1
                if tag != 1:
                    print('Nothing has been found.')

            #Back
            elif select == "5":
                break
        else:
            print('Please input the right index')


def login():
    try:
        dic = {}
        with open('user.txt', 'r') as file:
            for line in file:
                line = line.strip().split("|")
                dic[line[0]] = line[1:]
    except(FileNotFoundError):
        print("The file does not exist.")
    user = input('Please input the username: ')
    password = input('Please input the password: ')

    # Check username and password
    if user in dic.keys():
        if password == str(dic[user][0]):
            print("Login Successfully")
            # Normal user
            if dic[user][1] == "1":
                while True:
                    display_menu(MORMAL_USER)
                    select = input('Please input the index of choice: ')
                    if select in MORMAL_USER.keys():
                        if select == "1":
                            change_password(user, dic)
                        elif select == "2":
                            brows_this_user(user, dic)
                        else:
                            break
                    else:
                        print('Please input the right index')
            # Root user
            else:
                while True:
                    display_menu(ROOT_USER)
                    select = input('Please input the index of choice: ')
                    if select in ROOT_USER.keys():
                        if select == "1":
                            change_password(user, dic)
                        elif select == "2":
                            brows_this_user(user, dic)
                        elif select == "3":
                            brows_other_user(dic)
                        elif select == "4":
                            add_modify_delete_user(dic)
                        elif select == "5":
                            break
                    else:
                        print('Please input the right index')

        else:
            print("Your password or username is incorrect.")
    else:
        print("Your password or username is incorrect.")


def register():
    pass


def main():
    print('Welcome'.center(40, '-'))
    while True:
        # print main menu
        display_menu(MENU)
        select = input('Please input the index of choice: ')  # grep user's input
        if select in MENU.keys():  # identify wether the input is legal or not
            # login function
            if select == '1':
                login()
            # register function
            elif select == '2':
                try:
                    dic = {}
                    with open('user.txt', 'r') as file:
                        for line in file:
                            line = line.strip().split("|")
                            dic[line[0]] = line[1:]
                except(FileNotFoundError):
                    print("The file does not exist.")

                username = input('Please input the username: ')
                password = input('Please input the password: ')
                email = input('Please input the email: ')
                address = input('Please input the address: ')
                if username not in dic.keys():
                    dic[username] = [password, "1", email, address]
                    with open("user.txt", "w") as file:
                        for i in dic:
                            file.writelines("%s|%s\n" % (i, "|".join(dic[i])))
                    print('The user has been added successfully!')
                    login()
                else:
                    print("The user has existed.")
            else:
                break
        else:
            print('Please input the right index')


main()
