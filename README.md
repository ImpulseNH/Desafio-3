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
a
## Descripción de la solución
***
Para la solución de este problema se implementaron dos redes neuronales de tipo perceptrón multicapa, una con la librería Keras de Python y otra mediante una matriz de adyacencia. Dado que cada imagen es de 28x28 (784) pixeles y que existen 10 tipos de ropa para clasificar, se definió la siguiente cantidad de neuronas en las capas de entrada y salida, respectivamente:

* **Cantidad de neuronas en capa de entrada:** 784
* **Cantidad de neuronas en capa de salida:** 10

Por otro lado, a modo de poder realizar una comparación entre las dos formas de implementación, se definieron los siguientes parámetros en común:

* **Función de activación:** Sigmoide
* **Cantidad de capas ocultas:** 3
* **Cantidad de neuronas por capa oculta:** 4-6-4

En cuanto al optimizador, se utilizó `SGD` para la red neuronal con matriz de adyacencia, con un `learning rate` de `0.0005`. En cambio, para la red neuronal con Keras, se hicieron pruebas adicionales variando entre los optimizadores `Adam` y `SDG`, además de probar cada uno con y sin especificar `learning rate` (el mismo establecido en la red neuronal con matriz de adyacencia), con el fin de obtener resultados variados y realizar comparaciones más especificas.

## Análisis de resultados
***
c
## Cómo ejecutar el programa
***
Para poder probar el código es necesario abrir como proyecto la carpeta ```Desafio 3``` en un compilador compatible con Python.
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
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda | | | | |
2. **Integración**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        | | | | |
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda | | | | |
3. **Responsabilidad**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        | | | | |
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda | | | | |
4. **Contribución**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        | | | | |
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda | | | | |
5. **Resolución de conflictos**

|                     | Esteban González | Carlos Núñez | Priscilla Riffo | Katherine Sepúlveda |
| ------------------- | :--------------: | :----------: | :-------------: | :-----------------: |
| Esteban González    | |X|X|X|
| Carlos Núñez        | | | | |
| Priscilla Riffo     | | | | |
| Katherine Sepúlveda | | | | |
