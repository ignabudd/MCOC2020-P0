# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:41:35 2020

@author: ignab
"""

from scipy import rand
from time import perf_counter
from mimatmul import mimatmul



Ns = [2 , 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 150, 200, 250, 300, 500]
Ncorridas = 10


for i in range(Ncorridas):
    fid = open(f"matmul{i}.txt","w")
    dts = []  #timepo que se demora para cada matriz de tamaño N
    mem = []  # memoria que usa para cada matriz de tamaño N
    
    for N in Ns:
        print (f"N={N}")
        
        A = rand(N,N)
        B = rand(N,N)
        
        t1 = perf_counter()
        mimatmul(A,B)
        t2 = perf_counter()
         
        dt = t2 - t1
        size = 3 * (N**2) * 8
            
        dts.append(dt)
        mem.append(size)
         
        fid.write(f"{N} {dt} {size} \n")
            
        print(f"Tiempo transcurrido = {dt} s")
        print(f"Memoria usada = {size} bytes")
    
        fid.flush()
    
    fid.close()


from plotting import plotting #Esta función esta definida en otro archivo

plotting(Ncorridas)

