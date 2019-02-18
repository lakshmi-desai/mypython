# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:14:36 2019

@author: Lakshmi Desai
"""

def pay():
       
    try:
        h=int(input("Enter hours : "))
        r=int(input("Enter rate : "))
        if(h<=40):
            print(h*r)
        else:
            print((40*r)+(h-40)*1.5*r)
    except:
        print("Error, please enter numeric value")        
    
pay()
