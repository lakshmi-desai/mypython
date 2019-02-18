# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:57:05 2019

@author: Lakshmi Desai
"""

def convert():
    mydict={}
    a=input("Enter the string")
    a=a.split(";")
    for i in range(len(a)):
        x=a[i].split("=")  
        mydict.update({x[0]:x[1]})
    return mydict

d=convert()
print(d)

