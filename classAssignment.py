# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:18:34 2019

@author: Lakshmi Desai
"""

n=int(input())
flag=False
ans=[]
for i in range(n):
    s1=input()
    s2=input()
    
    if(len(s1)==len(s2) and s1!=s2):
        ans.append(-1)
    else:
        dele=[]
        d=0
        cur1=0
        cur2=0
        while(cur2<len(s2)):
            if(s1[cur1]==s2[cur2]):
                cur1+=1
                cur2+=1
            else:
                cur1+=1
                d+=1
                
            if(cur1!=len(s1) and cur2==len(s2)):
                flag=True
                dele.append(d)
                d=0
                cur2=0
            elif(cur1==len(s1) and cur2==len(s2)):
                dele.append(d)
                break
            elif(cur1==len(s1) and cur2!=len(s2)):
                break
                
        if(cur2!=len(s2)):
            ans.append(-1)
        elif(cur2==len(s2)):
            x=min(i for i in dele)
            ans.append(x)
            
for i in range(len(ans)):
    if(ans[i]==-1):
        print("No")
    else:
        print("Yes")
        print(ans[i])