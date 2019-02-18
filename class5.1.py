# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:36:30 2019

@author: Lakshmi Desai
"""
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

def pay():
     h=int(input("Enter hours : "))
     r=int(input("Enter rate : "))
     if(h<=40):
         return h*r
     else:
         return ((40*r)+(h-40)*1.5*r)
     
p=pay()
print(p)