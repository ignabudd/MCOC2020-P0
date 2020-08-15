# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:33:25 2020

@author: ignab
"""

import scipy as sp
import numpy as np
from time import perf_counter

N = 50

A = sp.matrix(sp.rand(N,N)) #Matriz principal a utlizar 
B = sp.matrix(sp.rand(N,N)) #Matriz secundaria
B1 = sp.matrix(sp.rand(N,1)) #vector de resultados, lado derecho


print (f"A = \n{A}")
print (f"B = \n{B}")

# multiplicacion de matrices

t1 = perf_counter()
C = A * B   #esto es multiplicacion de arreglos, por eso a las matrices se les agregó np.matrix
t2 = perf_counter()
dt = t2 - t1
print (f"El tiempo trancurrido de una multiplicación de matrices de 50 x 50 es de = {dt} s")
print (f"C = {C}")



# inversa de la matriz

print ("Forma 1 invertir matriz")
t3= perf_counter()
D0 = np.linalg.inv(A)  
t4 = perf_counter()
dt0 = t4 - t3
print (f"El tiempo trancurrido de la inversa de una matriz de 50 x 50 es de = {dt0} s")
print (f"D0 = {D0}")

print ("Forma 2 invertir matriz")
D1 = A**-1   
print (f"D1 = {D1}")

# resolver sistemas de ecuaciones

print ("Forma 1 Resolución sistemas de ecuaciones")
t5 = perf_counter()
x = np.linalg.solve(A,B1)
t6 = perf_counter()
dt1 = t6 - t5
print (f"El tiempo trancurrido de un sistema de ecuaciones es de = {dt1} s")
print (f"X = {x}")

print ("Forma 2 Resolución sistemas de ecuaciones") 
x1 = D1 * B1
print (f"X1 = {x1}")

# Valores y vectores propios

t7 = perf_counter()
valores, vectores = np.linalg.eig(A)
t8 = perf_counter()
dt2 = t8 - t7
print (f"El tiempo trancurrido para Valores y Vectores propios es de = {dt2} s")
print (f"Valores Propios = {valores}")
print (f"Vectores Propios = {vectores}")
 

#Multiplicacion de matrices muy grandes 

N = 1000

A = sp.matrix(sp.rand(N,N)) #Matriz principal a utlizar 
B = sp.matrix(sp.rand(N,N)) #Matriz secundaria

# multiplicacion de matrices

t9 = perf_counter()
C = A * B   #esto es multiplicacion de arreglos, por eso a las matrices se les agregó np.matrix
t10 = perf_counter()
dt3 = t10 - t9
print (f"El tiempo trancurrido para multiplicaciones de matrices de 1000 x 1000 es de = {dt3} s")


 


