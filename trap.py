# -*- coding: utf-8 -*-
"""
Created on Sun May 11 19:50:42 2025

@author: Mustafa Anjrini
"""

import numpy as np

def Trap(a,b,fun):
    f_a=fun(a) # calculating the first value of the integral
    f_b=fun(b) # calculating the last value of the integral
    f=f_a+f_b  # summing the above
    
    n=1000000 # number of divisions
    h=(b-a)/n # distance h

    # running the loop of the Trapezoidal rule
    for i in range(1,n):
        f+=2*fun(a+i*h)

    return f*h/2

a=0 #the lower bound of the integral, please change it accordingly
b=1000 # the upper bound of the integral, please change it accordingly

#here to write the function "fun" which we're gunna integrate
#please change it accordingly
def fun(x):
    return np.cos(x**2) 

# last step is to run the integration function to get the result
Trap(a,b,fun)



