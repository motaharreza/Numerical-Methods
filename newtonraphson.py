# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:23:14 2017
Newton Raphson Method to find the root of equation f(x)=0
@author: REZA
"""

def fuc(x):
    f=x**2-4 #given equation f(x)
    return f
def fucdas(x):
    fdas=2*x # derivative given equation f(x)
    return fdas

x0=float(input("Enter initial value root"))
for i in range(30):
    x1=x0-fuc(x0)/fucdas(x0)
    print(x1)
    if (abs(x0-x1))<0.001:
        break
    x0=x1


print ("The root of the equation f(x)=0 is x=",x1)