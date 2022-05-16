# Desafío 3
## Índice
1. [Descripción del problema](#descripción-del-problema)
2. [Descripción de la solución](#descripción-de-la-solución)
3. [Cómo ejecutar el programa](#cómo-ejecutar-el-programa)
4. [Análisis de resultados](#análisis-de-resultados)
5. [Video explicativo](#video-explicativo)
6. [Coevaluación](#coevaluación)
## Descripción del problema
***
Juan está interesado en el mercado de la venta de ropa en línea. Su revolucionaria idea implica usar una inteligencia artificial que recomiende ropa que se parezca. Para poder realizar esto, Juan deberá primero clasificar los tipos de ropa.

La ropa a clasificar está contenida en un Dataset, en donde cada prenda está identificada por un `label` que va desde 0 a 9, por lo que en total se tienen 10 tipos de prendas a clasificar. Cada `label` corresponde a las siguientes prendas:

```
0 - Polera
1 - Pantalón
2 - sweater
3 - Vestido
4 - Saco
5 - Sandalia
6 - Camisa
7 - Zapatilla
8 - Bolso/cartera
9 - Bota
```

Además, cada prenda está representada en una imagen de 28x28 pixeles, resultando en un vector de 784 pixeles por cada imagen de prenda. Cada pixel contiene un valor entre 0 y 1, siendo 0 completamente negro y 1 completamente blanco.

A partir de esto, el desafío planteado para la resolución de este problema es la implementación de una inteligencia artificial que haga el trabajo de ver y clasificar la ropa en los distintos tipos de prendas.
## Descripción de la solución
***
Para la solución de este problema se implementaron dos redes neuronales de tipo perceptrón multicapa, una con la librería Keras de Python y otra mediante una Matriz de Adyacencia. Dado que cada imagen es de 28x28 (784) pixeles y que existen 10 tipos de ropa para clasificar, se definió la siguiente cantidad de neuronas en las capas de entrada y salida, respectivamente:

* **Cantidad de neuronas en capa de entrada:** 784
* **Cantidad de neuronas en capa de salida:** 10

Por otro lado, a modo de poder realizar una comparación entre las dos formas de implementación, se definieron los siguientes parámetros en común:

* **Función de activación:** Sigmoide
* **Cantidad de capas ocultas:** 3
* **Cantidad de neuronas por capa oculta:** 4-6-4

Por lo tanto, para cada forma de implementación de la red neuronal, se tiene como topología:

* **Topología:** [784, 4, 6, 4, 10]

En cuanto al optimizador, se utilizó `SGD` para la red neuronal implementada con Matriz de Adyacencia, con un `learning rate` de `0.0005`. En cambio, para la red neuronal implementada con Keras, se hicieron pruebas adicionales variando entre los optimizadores `Adam` y `SDG`, además de probar cada uno con y sin especificar `learning rate` (de `0.0005`), con el fin de obtener resultados variados y realizar comparaciones más especificas.

Por último, para el proceso de entrenamiento se decidió dividir los datos en entrenamiento y pruebas de 70/30, y en aspectos de tiempo de entrenamiento, la red neuronal implementada con Keras se decidió entrenar en 100 épocas (Epoch), a diferencia de la red neuronal implementada con Matriz de Adyacencia que se decidió entrenar en 1000 iteraciones.
## Análisis de resultados
***
Después de todas las pruebas realizadas según lo propuesto en la sección anterior, se obtuvieron los siguientes resultados:

En primer lugar, se pudo observar que la red neuronal implementada con Keras obtuvo en general mejores resultados, dado que contenía en general una menor cantidad de falsos negativos y positivos para todos los tipos de prendas, demostrando una mejor precisión. Sin embargo, este resultado fue obtenido al entrenar la red con el optimizador `Adam`, ya que que al implementar el optimizador `SGD` los resultados fueron considerablemente menos precisos. Además, para obtener una buena calidad de resultados con Keras, se tuvo que dejar entrenando la red una mayor cantidad de tiempo, con un mínimo de 100 épocas (Epoch), que en promedio fueron de 5 a 6 minutos.

Por otra parte, si bien la red neuronal implementada con Matriz de Adyacencia obtuvo resultados menos precisos (mayor cantidad de falsos negativos y positivos), su tiempo de ejecución era considerablemente menor, siendo en promedio la mitad del tiempo de entrenamiento necesario para obtener buenos resultados con la red neuronal implementada con Keras. El problema con la implementación de esta red, fue que su aprendizaje solo se observó durante la etapa inicial de entrenamiento, luego de un tiempo se estancaba en cierto punto. A modo de comprobar si la cantidad de iteraciones era un factor influyente, se realizaron pruebas exhaustivas con una cantidad de iteraciones mayor a 10.000, pero ocurría el mismo fenómeno y el aprendizaje no demostraba progreso, por lo que deducimos que los parámetros definidos (función de activación, learning rate y topología) para esta forma implementación de red neuronal no fueron los más adecuados para el problema de este desafío.

En cuanto a los cambios de `learning rate` en la red neuronal implementada con Keras, no se logró obtener resultados mejores, por lo que se dejó sin especificar y se descartó realizar un análisis a este aspecto.

Cabe mencionar que después de todas las comparaciones realizadas, se pudo identificar un detalle interesante que ambas redes neuronales tenían en común. Ambas redes mostraban dificultad para clasificar las prendas de tipo **Camisa**, **Sweater** y **Saco**, donde particularmente para la prenda **Camisa** se obtuvo una cantidad de falsos negativos similar a la cantidad de falsos positivos para la prenda **Saco**, lo que nos permitió deducir que la similitud entre esas prendas hacia difícil la tarea de clasificación para las redes neuronales.

A partir del análisis realizado en esta sección, pudimos obtener como conclusión principal que
## Cómo ejecutar el programa
***
Para poder probar el código es necesario abrir como proyecto la carpeta `Desafio 3` en un compilador compatible con Python. Además, se deben tener instaladas las siguientes librerías:
* Keras
* Sklearn
* Seaborn
* Pandas
* Numpy
* Matplotlib

En el proyecto existen dos archivos en Python, los cuales corresponden a las redes neuronales implementadas con Keras y Matriz de Adyacencia, respectivamente. Estos son:

* keras.py
* matriz.py

## Video explicativo
***
Para una mejor comprensión del problema y su resolución, se adjunta un video explicativo en el siguiente [link]().
## Coevaluación
***
A continuación, tablas de coevaluación según estos criterios: [Criterios de coevaluación](https://docs.google.com/document/d/1YSba-KNP-ReP_TJePQkCHXJ1x4_MtOizQPIrNnriZbw/edit#)
1. **Asistencia y puntualidad**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        |X| |X|X|
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda |X|X|X |
2. **Integración**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        |X| |X|X|
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda |X|X|X|
3. **Responsabilidad**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        |X| |X|X|
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda |X|X|X| |
4. **Contribución**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        |X| |X|X|
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda |X|X|X| |
5. **Resolución de conflictos**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        |X| |X|X|
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda |X|X|X| |
