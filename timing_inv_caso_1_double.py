# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:41:44 2020

@author: ignab
"""

from scipy import zeros
from numpy import double, fill_diagonal, matrix
from numpy.linalg import inv
from time import perf_counter
import scipy as sp 
import matplotlib.pyplot as plt


Ns = [2 , 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 150, 200, 250, 300, 350, 500, 600, 800, 1000,2000,3000]
Ncorridas = 2

for i in range(Ncorridas):
    fid = open(f"caso_1_double{i}.txt", "w")        #cambiar
    dts = []  
    mem = []  
    
    for N in Ns:
        
        A = zeros((N,N))
        fill_diagonal(A, 2)
    
        for i in range(N):
            for j in range(N):
                if i+1 == j or i-1 == j:
                    A[i][j] = -1
                    
        A = double(A)               # Este va variando
        
        t1 = perf_counter()
        Ainv = inv(matrix(A))       #Ojo con este, es para single y double
        t2 = perf_counter() 
          
        dt = t2 - t1
        size = (N**2) * 8           # Double (8 Bytes - 64 bits), varía también
    
        
        dts.append(dt)
        mem.append(size)
         
        fid.write(f"{N} {dt} {size} \n")
        print (Ainv)    
        print(f"Tiempo transcurrido = {dt} s")
        print(f"Memoria usada = {size} bytes")
    
        fid.flush()
    
    fid.close()
    

#Plotting

def plotting(Ncorridas): 
    xtcks = [10,20,50,100,200,500,1000,2000, 5000,10000]

    ytcks = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 6*100]
    ytcklab = ["0.1 ms" , "1 ms" , "10 ms" , "0.1 s" , "1 s", "10 s", "1 min" , "10 min" ]

    ytcks2 = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10]
    ytcklab2 = [ "1 KB" , "10 KB" , "100 KB" , "1 MB" , "10 MB" , "100 MB", "1 GB", "10 GB"]
    
    data = sp.loadtxt("caso_1_double0.txt")     #cambiar
    
    Ns = data[:,0]
    dts = data[:,1]
    mem = data[:,2]
    
    
    for i in range (1, Ncorridas):
        data = sp.loadtxt(f"caso_1_double{i}.txt")      #cambiar
        dts = sp.vstack((dts, data[:,1]))
        
    plt.figure()
    
    plt.subplot(2,1,1)
    plt.loglog(Ns, dts.T, "-o")
    plt.ylabel("Tiempo Transcurrido")
    plt.title("Rendimiento A Inv -Caso 1 - Double")         # cambiar
    plt.grid(True)
    plt.xticks(xtcks, [])
    plt.yticks(ytcks, ytcklab)
    plt.tight_layout()
    
    
    plt.subplot(2,1,2)
    plt.loglog(Ns, mem, "-o")
    plt.xlabel("Tamaño de la matriz N")
    plt.ylabel("Memoria usada") 
    plt.grid(True)
    plt.xticks(xtcks, xtcks, rotation=45)
    plt.yticks(ytcks2, ytcklab2)
    plt.axhline(8000000000, linestyle="--", color="k")
   
    plt.show()

            
plotting(Ncorridas)    
    
    