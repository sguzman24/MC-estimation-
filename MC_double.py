#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 18:02:53 2023

@author: seth guzman
"""


import numpy as np
def MCinteg(f, x0, x1, y0, y1, n):
    """
    

    Parameters
    ----------
    f : TYPE
        DESCRIPTION.
    g : TYPE
        DESCRIPTION.
    x0 : TYPE
        DESCRIPTION.
    x1 : TYPE
        DESCRIPTION.
    y0 : TYPE
        DESCRIPTION.
    y1 : TYPE
        DESCRIPTION.
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    x = np.random.random(n)*(x1-x0)+x0
    y = np.random.random(n)*(y1-y0)+y0
    areaCount = 0
    
    for i in range(len(x)):
        xVal = x[i]
        for j in range (len(y)):
            yVal = y[j]
            if f(xVal) < yVal: areaCount +=1
            
    area = areaCount/(n**2)*(x1-x0)*(y1-y0)
    return area    
        
if __name__ == "__main__":
    def f(x):
        return x
    x0 = 0
    x1 = 1
    y0 = 0
    y1 = 1
    n = 500
    
    area = MCinteg(f, x0, x1, y0, y1, n)
    print(area)
  