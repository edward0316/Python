#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
import re

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
        statement = new_statement  # build the new statement
    print(new_statement) # build the new statement

statement = "2+3.5*3.4/2.1+4.7"
calcu(statement)


# str = "5.4*4.8*6*7"
# str1 = re.split(r"([\d\.]*\*[\d\.]*)", str)
# print(str1)