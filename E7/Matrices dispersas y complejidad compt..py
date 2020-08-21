# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:58:09 2020

@author: ignab
"""
 
from time import perf_counter
import numpy as np 
from numpy import zeros, double, fill_diagonal
import scipy.linalg as spLinalg
from scipy.sparse.linalg import inv, spsolve
from scipy.sparse import csc_matrix


def matriz_laplaceana_llena(N,d=double):
    A = zeros((N,N), dtype=d)
    fill_diagonal(A, 2)
    for i in range(N):
            for j in range(N):
                if i+1 == j or i-1 == j:
                    A[i][j] = -1
    
    return A  


def matriz_laplaceana_dispersa(N,d=double):
    A = zeros((N,N), dtype=d)
    fill_diagonal(A, 2)
    for i in range(N):
            for j in range(N):
                if i+1 == j or i-1 == j:
                    A[i][j] = -1
    
    return csc_matrix(A)   


Ns = [2 , 5, 10, 12, 15, 20, 30, 40, 45, 50, 
      55, 60, 75, 100, 125, 150, 200, 250, 300, 350,
      500, 600, 800, 1000, 2000, 3000, 5000, 8000]

Ncorridas = 5

nombres = ["Matmul_llena.txt", "Matmul_dispersa.txt", "Solve_llena.txt", "Solve_dispersa.txt",
           "Inv_llena.txt", "Inv_dispersa.txt"] 

archivos = [open(nombre, "w") for nombre in nombres]

for N in Ns:
    dts0 = np.zeros((Ncorridas, len(archivos)))
    dts1 = np.zeros((Ncorridas, len(archivos)))
    print (f"N = {N}")
    
    for i in range(Ncorridas):
        
                #COMPLEJIDAD ALGORÍTMICA DE MATMUL - CASO 1
        
        # Matriz llena y tipo double - Multiplicación A*B
        t1 = perf_counter()
        A = matriz_laplaceana_llena(N)
        B = matriz_laplaceana_llena(N)
        t2 = perf_counter()
        C = A@B
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2

        dts0[i][0] = dt1
        dts1[i][0] = dt2
        
        # Matriz dispersa y tipo double - Multiplicación A*B
        t1 = perf_counter()
        A = matriz_laplaceana_dispersa(N)
        B = matriz_laplaceana_dispersa(N)
        t2 = perf_counter()
        C = A@B
        t3 = perf_counter()
        dt1 = t2 - t1 
        dt2 = t3 - t2

        dts0[i][1] = dt1
        dts1[i][1] = dt2
        
                #COMPLEJIDAD ALGORÍTMICA DE SOLVE - CASO 2
        
        # Matriz llena y tipo double - Sist. Ecuaciones Ax=b
        t1 = perf_counter()
        A = matriz_laplaceana_llena(N)
        B = np.ones(N)
        t2 = perf_counter()
        C = spLinalg.solve(A,B) 
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2

        dts0[i][2] = dt1
        dts1[i][2] = dt2
        
        # Matriz dispersa y tipo double - Sist. Ecuaciones Ax=b
        t1 = perf_counter()
        A = matriz_laplaceana_dispersa(N)
        B = np.ones(N)
        t2 = perf_counter()
        C = spsolve(A,B) 
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2

        dts0[i][3] = dt1
        dts1[i][3] = dt2
        
                #COMPLEJIDAD ALGORÍTMICA DE INV - CASO 3
        
        # Matriz llena y tipo double - Inviertiendo matriz A
        
        t1 = perf_counter()
        A = matriz_laplaceana_llena(N)
        t2 = perf_counter()
        B = spLinalg.inv(A) 
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2

        dts0[i][4] = dt1
        dts1[i][4] = dt2
        
        # Matriz dispersa y tipo double - Inviertiendo matriz A
        
        t1 = perf_counter()
        A = matriz_laplaceana_dispersa(N)
        t2 = perf_counter()
        B = inv(A) 
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2

        dts0[i][5] = dt1
        dts1[i][5] = dt2
        
        dts_mean0 = [np.mean(dts0[:,j]) for j in range(len(archivos))]
        dts_mean1 = [np.mean(dts1[:,j]) for j in range(len(archivos))]
    
    for j in range(len(archivos)):
        archivos[j].write(f"{N} {dts_mean0[j]} {dts_mean1[j]}\n")
        archivos[j].flush()

[archivo.close() for archivo in archivos]


        
       
       
       
       
    


























