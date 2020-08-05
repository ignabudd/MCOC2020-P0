# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:33:25 2020

@author: ignab
"""

import scipy as sp
import numpy as np

N = 4

A = sp.matrix(sp.rand(N,N)) #Matriz principal a utlizar 
B = sp.matrix(sp.rand(N,N)) #Matriz secundaria
B1 = sp.matrix(sp.rand(N,1)) #vector de resultados, lado derecho


print (f"A = \n{A}")
print (f"B = \n{B}")

# multiplicacion de matrices

C = A * B   #esto es multiplicacion de arreglos, por eso a las matrices se les agregó np.matrix
print (f"C = {C}")

# inversa de la matriz

print ("Forma 1 invertir matriz")
D0 = np.linalg.inv(A)  
print (f"D0 = {D0}")

print ("Forma 2 invertir matriz")
D1 = A**-1   #inversa de la matriz
print (f"D1 = {D1}")

# resolver sistemas de ecuaciones

print ("Forma 1 Resolución sistemas de ecuaciones")
x = np.linalg.solve(A,B1)
print (f"X = {x}")

print ("Forma 2 Resolución sistemas de ecuaciones")
x1 = D1 * B1
print (f"X1 = {x1}")

# Valores y vectores propios

valores, vectores = np.linalg.eig(A)

print (f"Valores Propios = {valores}")

print (f"Vectores Propios = {vectores}")


#Multiplicacion de matrices muy grandes 

N = 150

A = sp.matrix(sp.rand(N,N)) #Matriz principal a utlizar 
B = sp.matrix(sp.rand(N,N)) #Matriz secundaria


print (f"A = \n{A}")
print (f"B = \n{B}")

# multiplicacion de matrices

C = A * B   #esto es multiplicacion de arreglos, por eso a las matrices se les agregó np.matrix
print (f"C = {C}")






