# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:30:35 2020

@author: ignab
"""

import numpy as np

def mimatmul1(A,B):
    print ("Implementar matmul a mano")
    C = np.dot(A,B)
    return C


def mimatmul(A,B):
    print ("Implementar matmul a mano")
    res =[]
    for a in range(len(A)):
        row = []
        for b in range(len(A)):
            row.append(0)
        res.append(row)
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k]*B[k][j]
                
    
    return res
