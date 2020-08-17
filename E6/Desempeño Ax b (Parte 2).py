# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:13:22 2020

@author: ignab
"""

import scipy as sp 
from time import perf_counter
import numpy as np 
from numpy import zeros, float32, fill_diagonal
import matplotlib.pyplot as plt
import scipy.linalg as spLinalg

def matriz_laplaceana(N,d=float32):
    A = zeros((N,N), dtype=d)
    fill_diagonal(A, 2)
    for i in range(N):
            for j in range(N):
                if i+1 == j or i-1 == j:
                    A[i][j] = -1
    
    return A

Ns = [2 , 5, 10, 12, 15, 20, 30, 40, 45, 50, 
      55, 60, 75, 100, 125, 150, 200, 250, 300, 350,
      500, 600, 800, 1000, 2000,3000,5000]

Ncorridas = 10

nombres = ["A_invB_inv.txt", "A_invB_npsolve.txt", "A_invB_spsolve.txt", "A_invB_spsolve_symmetric.txt",
           "A_invB_spsolve_pos.txt","A_invB_spsolve_pos_overwrite.txt"] 

archivos = [open(nombre, "w") for nombre in nombres]

for N in Ns:
    dts = np.zeros((Ncorridas, len(archivos)))
    print (f"N = {N}")
    
    for i in range(Ncorridas):
        
        #Forma 1, invertir  multiplicar
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B
        t2 = perf_counter()
        dt = t2 - t1
        
        dts[i][0] = dt
        
        #Forma 2, usando np.linalg.solve(A,B)
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        
        dts[i][1] = dt
        
        #Forma 3, usando spLinalg(A,B)
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        
        dts[i][2] = dt
        
        
        #Forma 4, usando symmetric de scipy
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A,B,assume_a="sym")
        t2 = perf_counter()
        dt = t2 - t1
        
        dts[i][3] = dt
        
        #Forma 5, usando pos de scipy
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A,B,assume_a="pos")
        t2 = perf_counter()
        dt = t2 - t1
        
        dts[i][4] = dt
        
        #Forma 6, usando pos y overwrite_a de scipy
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = spLinalg.solve(A,B,assume_a="pos", overwrite_a=True)
        t2 = perf_counter()
        dt = t2 - t1
        
        dts[i][5] = dt
        
        
    print ("dts: ", dts)
    
    dts_mean = [np.mean(dts[:,j]) for j in range(len(archivos))]
    
    print ("dts_mean: ", dts_mean)
    
    for j in range(len(archivos)):
        archivos[j].write(f"{N} {dts_mean[j]}\n")
        archivos[j].flush()

[archivo.close() for archivo in archivos]


def plotting(nombres):
    xtcks = [10,20,50,100,200,500,1000,2000, 5000,10000]

    ytcks = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 6*100]
    ytcklab = ["0.1 ms" , "1 ms" , "10 ms" , "0.1 s" , "1 s", "10 s", "1 min" , "10 min" ]
    
    plt.figure()
    
    for nombre in nombres:
        data = sp.loadtxt(nombre)
        Ns = data[:, 0]
        dts = data[:, 1]
        
        print ("Ns: ", Ns)
        print ("dts: ", dts)
        
        plt.loglog(Ns, dts.T, "-o", label=nombre)
        plt.xlabel("Tamaño de la matriz N")
        plt.ylabel("Tiempo Transcurrido")
        plt.title("Desempeño Ax=B")         
        plt.grid(True)
        plt.xticks(xtcks, xtcks, rotation=45)
        plt.yticks(ytcks, ytcklab)
        plt.tight_layout()
        
    plt.tight_layout()
    plt.legend()
    plt.show()
    

plotting(nombres)


      