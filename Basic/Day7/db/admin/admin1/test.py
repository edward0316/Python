#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

from xml.etree import ElementTree as ET

tree = ET.parse("profile.xml")
root = tree.getroot()
for i in root.iter("password"):
    print(i.tag)
# for child in root:
#     print(child.tag, child.text)
# print(root.tag)
# print(tree)
# print(root)


