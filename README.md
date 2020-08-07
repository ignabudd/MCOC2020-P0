# MCOC2020-P0

# Mi computador principal

+ Marca/Modelo: HP 250 G4 
+ Tipo: Notebook
+ Año Adquisión: 2015
+ Procesador:
  + Marca/Modelo: Intel Pentium Processor 3825U
  + Velocidad Base: 1.9 GHz
  + Velocidad Máxima: 1.9 GHz
  + Número de Núcleos: 4
  + Número de Hilos: 2
  + Arquitectura: x64
  + Set de instrucciones: Intel SSE4.1, Intel SSE4.2
 
+ Tamaño de las cachés del computador:
  + L1 D: 32 KB x 2
  + L1 I: 32 KB x 2
  + L2: 256 KB
  + L3: 2 MB
  
+ Memoria:
  + Total: 8 GB
  + Tipo de memoria: DDR3
  + Velocidad: 1896.8 MHz
  + Numero de (SO)DIMM: 4
  
+ Disco 1:
  + Marca: WDC WD10JPVX-60JC3T0
  + Tipo: HDD
  + Tamaño: 1 TB
  + Particiones: 1
  + Sistema de archivos: NTFS 

+ Dirección MAC de la red wifi inalámbrica: A8-A7-95-A2-31-E9

+ Dirección IP (Interna, del router): 192.168.1.9

+ Dirección IP (Externa, del ISP): 190.215.0.18

+ Proveedor internet: GTD Manquehue S.A

# Desepeño MATMUL  
  
![Rendimiento AB tiempo](https://user-images.githubusercontent.com/69213519/89678665-96e17d00-d8bd-11ea-994b-c4f9e09911ce.png)
![Rendimiento AB memo](https://user-images.githubusercontent.com/69213519/89678672-99dc6d80-d8bd-11ea-9c62-216a53861a6a.png)
+ ¿Como difiere del gráfico del profesor/ayudante?
  + Se aprecia una clara diferencia en las matrices más grandes, en donde en el gráfico del profesor se observa una demora de 1 min para matrices de 10000 x 100000, y en mi computador, se demora eso en matrices de 5000 x 5000. Para las matrices más chicas ocurre el mismo patrón, mi computador de demora aprox 0.1 ms, mientras que el del profesor, para matrices entre 2 x 2 hasta 50 x 50, se demora menos de 0.1 ms.
  + El gráfico de desempeño de la memoria usada se obsrva que, para matrices de 10000x10000, el pc del profesor usa 1 GB de memoria (o incluso más), mientras que en el mio, ese es el límite, con matrices de 5000 x 5000.
+ ¿A qué se pueden deber las diferencias?
+ El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
+ ¿Qué versión de python está usando?
  + versión 3.8.3
+ ¿Qué versión de numpy está usando?
  + Numpy: 1.18.5
  + Scipy : 1.5
+ Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
 

