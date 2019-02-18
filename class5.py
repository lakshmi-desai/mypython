# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:14:36 2019

@author: Lakshmi Desai
"""

def pay():
    h=int(input("Enter hours : "))
    r=int(input("Enter rate : "))
    
    if(h<=40):
        return h*r
    else:
        return ((40*r)+(h-40)*1.5*r)
    
p=pay()
print(p)