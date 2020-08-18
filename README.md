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
  
+ Tarjeta de video integrada:
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

# Desempeño MIMATMUL 

![Desempeño MIMATMUL](https://user-images.githubusercontent.com/69213519/89836874-b08cf980-db35-11ea-927e-1cab9ddcefb4.png)

+ ¿Como difiere del gráfico del profesor/ayudante?
  + El gráfico del ayudate difiere enormemente en las matrices de mayor tamaño, ya que, su computador se demora 10 min para matrices de 1000 x 1000, en donde en el mio se demora eso para matrices de 500 x 500, sin embargo, para las matrices más chcas, se comportan de manera muy similar en relación al tiempo.
  + Con respecto a la meoria utilizda, se puede observar que mi gráfico con el del ayudante son muy parecidos, sin embargo a medida que va aumentando el tamaño de la matiz, mi computador utiliza más memoria.
+ ¿A qué se pueden deber las diferencias?
  + Esto se puede deber a que lo mas probable es que el aydante tenga un procesador mejor que el mio, una mayor memoria RAM, y más memoria caché, ya que el mio tiene muy poco de estas, y un procesador básico. 
+ Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
  + se hizo una prueba con 10 corridas y se puede ver se está utilizando un procesador. 
![Desempeño MIMATMUL CPU](https://user-images.githubusercontent.com/69213519/89852134-302dbf00-db5c-11ea-98e8-48d2d75c082e.PNG)

# Desempeño INV

  + Tamaños de memoria
    + Half: 2 bytes
    + Single: 4 bytes
    + Double: 8 Bytes
    + Longdouble: 8 Bytes

  + Análisis desempeño 
    # Caso 1: Numpy.linalg.inv
    - En este caso no se pudo ejecutar no.half ni np.logdouble, pues no son compatibles con este.
    - El desempeño de np.single y np.double es bastante similar 
    - Se pudo observar en ambos casos el procesador estaba trabajando en aproximadamente un 56%
    - Para matrices de 1000 x 1000, para ambos se obtuvo un tiempo de 0.15 ms y una memoria de 5 MB.
    - A continuación se muestran los gráficos para cada tipo:
    
    ![Caso_1_Single](https://user-images.githubusercontent.com/69213519/90063048-bfe78080-dcb6-11ea-9da2-02f1b17e1e1f.png)
    ![Caso_1_Double](https://user-images.githubusercontent.com/69213519/90063045-beb65380-dcb6-11ea-858f-403ea97bb673.png)
    
    # Caso 2: scipy.linalg.inv, overwrite=False
    - Se logró observar que el procesador se ejecutaba a un 70% aproximadamente, este es más alto que en el caso 1.
    - Para matrices grandes de 3000 x 3000 so observó que para tipos de datos half se demoró 5 s y ocupó 5 MB, en cambio para datos de tipo longdouble, se demoro 10 s y ocupó 100 MB para el mismo tamaño de matriz. Además, para el long double y double ocupa la misma memoria en el caso de mi pc.
    - A continuación se muestran los gráficos para cada dtype:
    
    ![Caso_2_Half](https://user-images.githubusercontent.com/69213519/90063255-1654bf00-dcb7-11ea-90e5-fd2975710d8d.png)
    ![Caso_2_Single](https://user-images.githubusercontent.com/69213519/90063505-7cd9dd00-dcb7-11ea-85b3-4679e9f128af.png)
    ![Caso_2_Double](https://user-images.githubusercontent.com/69213519/90063320-2a002580-dcb7-11ea-8587-03b8efa19ae1.png)
    ![Caso_2_LongDouble](https://user-images.githubusercontent.com/69213519/90070728-58cfc900-dcc2-11ea-8dae-2466d8729a68.png)

    # Caso 3: scipy.linalg.inv, overwrite=True
    
    - En este caso se logró que el procesador funcionara a un 86% aprox, lo que se debe a la condición overwrite=True.
     - Se puede bservar que para matrices de 3000 x 3000, con el tipo half, se demora 7 s y usa una memoria de 20 MB, en cambio con datos longdouble,se demora 5 s y usa una memoria de 100 MB. Además, para el long double y double ocupa la misma memoria en el caso de mi pc. Se puede concluir que este caso si resulta una ganancia de desempeño con la condición, además es el más eficiente. 
    
    ![Caso_3_Half](https://user-images.githubusercontent.com/69213519/90064441-c8d95180-dcb8-11ea-8f10-1f5f2d03fdb1.png)
    ![Caso_3_Single](https://user-images.githubusercontent.com/69213519/90064447-c971e800-dcb8-11ea-9c55-b2ce95d3a545.png)
    ![Caso_3_Double](https://user-images.githubusercontent.com/69213519/90064439-c840bb00-dcb8-11ea-902a-ff4f45e1e001.png)
    ![Caso_3_LongDouble](https://user-images.githubusercontent.com/69213519/90070682-435a9f00-dcc2-11ea-9f25-2cae469eddb7.png)

+ Análisis gráficos
   + Como se puede observar en los gráficos anteriores, el tipo de datos más eficiente se encuentra entre el np.half y np.single, donde los tiempos que se demora para matrices de tamaño 2000, es de 1 s. En cambio, para los tipos de datos np.double y np.longdouble (que ocupan la misma memoria), estos se demoran 3-4 s para matrices de ese tamaño.
+ ¿Qué algoritmo de inversión cree que utiliza cada método?
  + Para todos los casos se utiliza Invertible Matrix, esta verifica que el determinante sea distinto de cero, es decir que sea singular, además debe ser cuadrada. Para el primer caso se usa un algoritmo con la libreria numpy, np.linalg.inv, que creo que utiliza eliminación de Gauss o una alternativa a esto es la descomposición LU. Para los dos siguiente con la libreria scipy, creo que usa Cailey-Hamilton, pues permite obtener el determinante y con esta misma matriz se obtienen las siguientes operaciones. 
  + También se utiliza Matriz laplaciana, esta es la representacion matricial de un grafo, en donde en este caso la diagonal tiene un vaor de 2, y sus diagonales en las posiciones i+1 e i-1 tienen un valor de -1. El resto de las posiciones tiene un valor de 0. 
+ ¿Cómo incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso?
  + El paralelismo significa que el procesador del comptador puede realizar varias actividades o tareas al mismo tiempo, por lo que su rendimiento se va a ver afectado si es que se estan ejecutando otros procesos, lo que hace es que el procesador divide ls problemas más grandes en más pequeños. En este caso, se ve afetado su desempeño por los tipos de datos en cada caso y por la otras tareas que se están ejecutando. La estructura caché permite que los nucleos y servidores trabajen sobre los datos en paralelo, aprovechando al máximo la potencia, utilizando L1, L1 y L3.
  
 # Desempeño Ax=b (Parte 1)
 
 ![Grafico desempeño Ax b](https://user-images.githubusercontent.com/69213519/90294770-37531680-de55-11ea-8c65-ef2eff04f51e.png)
  + El máximo tamaño de matrices que corri fue de N = 5000, pues con una de N = 10000 se demoraba mucho tiempo en correr, mas de 10 minutos. En esta primera mencionada, se observa que se demoró aproximadamente 2 min para el caso de ivertir la matriz y luego multiplicarla por el vector, en cambio, para el caso de que lo resuelve de manera npsolve(A,B) se demoró 20-30 segundos aprox. eN comparación al gráfico del ayudante, el de él se demoraba 1 s y menos de 1 s para matrices de ese tamaño, en ambos casos respectivamente. Se logra concluir que np.solve(A,B) es más eficiente, tiene un mejor rendimiento, ya que no realiza dos cálculos (dos pasos), como en el otro caso. 

 # Desempeño Ax=b (Parte 2)
 
 ![Grafico desempeño Ax b (Parte 2)](https://user-images.githubusercontent.com/69213519/90460531-029fc300-e0d2-11ea-9fb3-2606f4243cdb.png)
 + Para medir el desempeño corrí para un tamaño de matrices desde N = 2 hasta N = 5000, con 10 coridas cada una, ya que probando con N = 10000 y 5 corridas se demoraba más de media hora en correr el programa entero. 
 + Gracias al gráfico se puede observar que para matrices mas pequeñas (de tamaño N = 2 hasta N = 40) el método más rápido es np.solve de Numpy (color naranjo), mientras que los otros métodos se demoran un tiempo similar a este, al rededor de 0.1 ms.
 + Se puede observar que la matrices de al rededor de tamaño N = 50 presentan algunos peaks con los solvers. Esto se puede deber a que el computador empieza a utilizar más el procesador, es decir con un mayor porcentaje. 
 + Para matrices muy grandes se logra apreciar una diferencia entre los solver de mayor y menor eficiencia. La función mas lenta es A_invB_inv, la cual era de esperarse, pues invierte la matriz y luego la multiplica por el vector de unos, en vez de utilizar directamente el solver. El solver np.solve no destaca entre los más rápidos para matrices grandes, el cual presenta una demora bastante parecida al solver de Scipy sp.solve.
 + Por último, para los solvers de scipy, destaca el más rápido cuando se detalla que la matriz es simétrica y positiva (color café), es decir la función A_inv_spsolve_pos_overwrite, pues esta optimiza el cálculo de manera que puede sobreescribir y además toma los valores del triangulo de arriba.  
 
