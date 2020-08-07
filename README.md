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
  
+ Tarjeta Gráfica:
  + Marca/Modelo: Intel(R) HD Graphics 
  + Memoria: 4181 MB
  + Resolución: 1366 x 768 
  
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
  + Las diferencias principalmente son porque el computador del profesor tiene un muy buen procesador, en comparación al mio, también él tiene 32 GB de memoria RAM,cuando yo tengo solo 8 GB. Por último, las cachés del profesor son mucho más altas. Todo esto hace que funcione a una velocidad muy superior al mio.  
+ El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  + El gráfico de uso de meoria es lineal ya que como cada unidad guardada en una matriz ocupa 8 bytes, es decir una matriz de 10 x 10, tiene 100 unidades guardadas, por lo que esa matriz ocupa 800, luego, al multiplicarla por otra de 10 x 10, se obtiene una tercera matriz. Obteniendo un total de 2400 bytes, o 2.4 KB para las 3 matrices. Es por esto que mientras más grande sea la matriz más bytes ocupara, o sea más memoria, esto aumenta linealmente.
  + El caso del gráfico del tiempo transcurrido no es lineal ya que cada vez que se inicia un proceso, este tiene variadas maneras distintas de empezar, además varía el tiempo si es que uno está utilizando otras aplicaciones al mismo tiempo de la ejecución del programa. 
+ ¿Qué versión de python está usando?
  + Versión 3.8.3
+ ¿Qué versión de numpy está usando?
  + Numpy: 1.18.5
  + Scipy : 1.5
+ Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
  + Se hizo una prueba con 5 corridas, y se utliza solo un procesador, como se puede ver a continuación.
 ![Uso procesador con 5 corridas](https://user-images.githubusercontent.com/69213519/89687242-d6b06080-d8cd-11ea-8a70-b1d981cb4b55.PNG)


