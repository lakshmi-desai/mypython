# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:28:47 2019

@author: Lakshmi Desai
"""

def convert():
    mylist=list()
    a=input("Enter the string")
    a=a.split(";")
    for i in a:
        x=i.split("=")
        mylist.append((x[0],x[1]))
    return mylist

d=convert()
print(d)