#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward
# import os
# from xml.etree import ElementTree as ET
#
# tree = ET.parse("profile.xml")
# root = tree.getroot()
# print(root)
# a = root.find("abcghj/password")
# print(a.text)

# for i in root.find("abc"):
#     print(i.tag, i.text, )
#print(root[1].tag)

#coding=utf-8
# import  xml.dom.minidom
#
# #打开xml文档
# dom = xml.dom.minidom.parse('profile.xml')
#
# #得到文档元素对象
# root = dom.documentElement
# # print(root.nodeName)
# # print(root.nodeValue)
# # print(root.nodeType)
# # print(root.ELEMENT_NODE)
#
# bb = root.getElementsByTagName('abc')
# b= bb[0]
# print(b.nodeName)

# class Foo:
#     def __init__(self):
#         ret = getattr(self, "plus")
#         print(hasattr(self, "plus"))
#         t = ret()
#
#     def plus(self):
#         print("plus")
#         print("haha")
#
# t = Foo()
# ret = getattr(t, "plus")
# print(ret)
# t = ret()

# import sys
# import time
#
#
# def view_bar(num, total):
#     rate = num / total
#     rate_num = int(rate * 100)
#     r = '\r[%s%s]%d%%' % ("=" * num, " " * (100 - num), rate_num,)
#     sys.stdout.write(r)
#     sys.stdout.flush()
#
#
# if __name__ == '__main__':
#     for i in range(0, 101):
#         time.sleep(0.1)
#         view_bar(i, 100)

import os
print(os.path.dirname(__file__))
print(os.getcwd())
os.chdir(os.path.join(os.path.dirname(__file__), "abc"))
print(os.getcwd())
print(os.path.abspath(__file__))

path = "abc\\temp"
path_list = path.split("\\")
print(path_list)
t = os.path.dirname(__file__)
for i in path_list:
    t = os.path.join(t,i)
print(t)
os.chdir(t)
print(os.getcwd())
