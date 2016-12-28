#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import re

def bracket(statement):
    while len(re.split(r"(\([0-9\+\-\*\/\.]*\))", statement)) > 1: #check the satement that is there any brackets
        new_statement = ""
        temp = re.split(r"(\([0-9\+\-\*\/\.]*\))", statement) #find out the first brakets which there is not any other bracket in it.
        temp1 = re.split(r"\(([0-9\+\-\*\/\.]*)\)", temp[1]) #exclude the symbol
        r1 = calcu(temp1[1]) #send the statement to calcu function to calcutate
        #using the result and the rest of the satement to assemble a new statement
        temp[1] = r1
        for i in range(0, len(temp)):
            new_statement = new_statement + str(temp[i])
        statement = new_statement
    #send the statement whithout bracket to calculator.
    calcu(statement, 1)


def calcu(statement, flag=0):
#Calculate multiplication and division firstly
    while len(re.split(r"([\d\.]*[\*/][\d\.]*)",statement)) > 1: #check the statement that is there any multiplicaions or divisions
        new_statement = ""
        temp = re.split(r"([\d\.]*[\*/][\d\.]*)",statement) #seperate the statement by the first multiplication or division
        temp1 = re.split(r"([\*/])", temp[1])

        #calculate multiplications and divisions
        if temp1[1] == "*":
            temp[1] = str(float(temp1[0]) * float(temp1 [2]))
        elif temp1[1] == "/":
            temp[1] = str(float(temp1[0]) / float(temp1 [2]))
        for i in range(0,len(temp)):
            new_statement = new_statement + temp[i]
        statement = new_statement # build the new statement

    temp = re.split(r"([+-])", statement)
    #calculate plus and minus
    while len(temp) > 3:
        temp2 = []
        if temp[1] == "+":
            temp1 = float(temp[0]) + float(temp[2])
        elif temp[1] == "-":
            temp1 = float(temp[0]) - float(temp[2])
        temp2.append(temp1)
        for i in range(3,len(temp)):
            temp2.append(temp[i])
        temp = temp2
    if temp[1] == "+":
        temp = float(temp[0]) + float(temp[2])
    elif temp[1] == "-":
        temp = float(temp[0]) - float(temp[2])
    #judge the calculation is the last calculation, and print out the result
    if flag != 0:
        print(temp)
    return temp

    #print(statement)

if __name__ == '__main__':
    #statement = input("Input statement: ")
    statement = "2-1.4*(12-1+52)+2/3"
    # calcu(statement)
    #statement = "9+5*(3+6)-(8/4+4*(5+6))"
    bracket(statement)
