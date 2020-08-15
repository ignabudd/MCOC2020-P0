# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:58:07 2020

@author: ignab
"""
import scipy as sp 
from matplotlib import pyplot as plt




def plotting(Ncorridas): 
    xtcks = [10,20,50,100,200,500,1000,2000, 5000,10000]

    ytcks = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 6*100]
    ytcklab = ["0.1 ms" , "1 ms" , "10 ms" , "0.1 s" , "1 s", "10 s", "1 min" , "10 min" ]

    ytcks2 = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10]
    ytcklab2 = [ "1 KB" , "10 KB" , "100 KB" , "1 MB" , "10 MB" , "100 MB", "1 GB", "10 GB"]
    
    data = sp.loadtxt("matmul0.txt")
    
    Ns = data[:,0]
    dts = data[:,1]
    mem = data[:,2]
    
    
    for i in range (1, Ncorridas):
        data = sp.loadtxt(f"matmul{i}.txt")
        dts = sp.vstack((dts, data[:,1]))
        
    plt.figure()
    
    plt.subplot(2,1,1)
    plt.loglog(Ns, dts.T, "-o")
    plt.ylabel("Tiempo Transcurrido")
    plt.title("Rendimiento A@B")
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
    plt.axhline(1000000000, linestyle="--", color="k")
   
    plt.show()






















