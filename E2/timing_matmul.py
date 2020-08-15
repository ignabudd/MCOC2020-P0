# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:48:15 2020

@author: ignab
"""


from scipy import rand
from time import perf_counter


Ncorridas = 10
Ns = [2 , 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 150, 200, 250, 350, 500, 600, 800,1000,2000,5000] 

for i in range(Ncorridas):
    dts = []  #timepo que se demora para cada matriz de tamaño N
    mem = []  # memoria que usa para cada matriz de tamaño N
    
    name = (f"matmul{i}.txt")
    fid = open(name, "w")
    
    for N in Ns:
        
        print (f"N={N}")
        A = rand(N,N)
        B = rand(N,N)
    
        t1 = perf_counter()
        C = A@B
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
    

    
from plotting import plotting 

plotting(Ncorridas)

        
        
