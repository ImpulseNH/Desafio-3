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

En cuanto al optimizador, se utilizó `SGD` para la red neuronal implementada Matriz de Adyacencia, con un `learning rate` de `0.0005`. En cambio, para la red neuronal implementada con Keras, se hicieron pruebas adicionales variando entre los optimizadores `Adam` y `SDG`, además de probar cada uno con y sin especificar `learning rate` (de `0.0005`), con el fin de obtener resultados variados y realizar comparaciones más especificas.

Por último, para el proceso de entrenamiento se decidió dividir los datos en entrenamiento y pruebas de 70/30. En aspectos de tiempo de entrenamiento, la red neuronal implementada con Keras se entrenó en 100 épocas (Epoch) y la red neuronal implementada con Matriz de Adyacencia se entrenó en 1000 iteraciones.
## Análisis de resultados
***
c
## Cómo ejecutar el programa
***
Para poder probar el código es necesario abrir como proyecto la carpeta ```Desafio 3``` en un compilador compatible con Python. Además, se deben tener instaladas las siguientes librerías:
* Keras
* Sklearn
* Seaborn
* Pandas
* Numpy
* Matplotlib

En el proyecto existen dos archivos en Python, los cuales corresponden a las redes neuronales implementadas con Keras y Matriz de Adyacencia, respectivamente:

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
| Carlos Núñez        | | | | |
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda | | | | |
2. **Integración**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        | | | | |
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda | | | | |
3. **Responsabilidad**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        | | | | |
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda | | | | |
4. **Contribución**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        | | | | |
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda | | | | |
5. **Resolución de conflictos**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        | | | | |
| Priscilla Riffo     |X|X| |X|
| Katherine Sepúlveda | | | | |
