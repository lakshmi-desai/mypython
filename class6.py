# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:26:28 2019

@author: Lakshmi Desai
"""

def score():
    try:
        s=float(input("Enter Score : "))
        
        if(s<0.0 or s>1.0):
            print("bad score")
        else:
            if(s>=0.9):
                print("A")
            elif(s>=0.8):
                print("B")
            elif(s>=0.7):
                print("C")
            elif(s>=0.6):
                print("D")
            else:
                print("F")
    except:
        print("bad score")
            
score()