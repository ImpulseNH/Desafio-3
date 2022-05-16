import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, multilabel_confusion_matrix, precision_score
import time 
import seaborn as sns
import matplotlib.pyplot as plt

# leer dataset
dataset = pd.read_csv('https://raw.githubusercontent.com/OptativoPUCV/Fashion-DataSet/master/fashion-1.csv')
print("Dataset leído.")
dataset.head(5)
#print(dataset)

# obtener valores
tipos = pd.get_dummies(dataset['label']) #lista de tipos
images = dataset.drop(columns=['label']) #imagenes
#print(tipos)
#print(images)

# dividir en train&test
tipos_train, tipos_test, images_train, images_test = train_test_split(tipos, images, test_size=0.3, random_state=2)
#normalizar los valores de los pixeles
images_train = (images_train - images_train.mean()) / images_train.std() + 0.0001
images_test = (images_test - images_test.mean()) / images_test.std() + 0.0001

print("- TIPOS: ")
print(tipos_train)
print("- IMAGENES: ")
print(images_train)

def activation(x):
  return ((1/(1+np.e**(-x))) , (x * (1-x)))
  # RELU
  # return ((np.maximum(0,x)), (np.where(x<0,0,1)))

class Capa():
  def __init__(self, n_conexiones: int, n_neuronas: int, activation):
    self.activation = activation
    self.W = np.random.rand(n_conexiones, n_neuronas) * 2 - 1

def crear_red(topologia: list, activation):
  red = []
  for l, capa in enumerate(topologia[:-1]):
    red.append( Capa(topologia[l], topologia[l+1], activation) )
  return red

def forward(red, images):
  out = [(None, images)]
  for l, capa in enumerate(red):
    z = out[-1][1] @ red[l].W # Multiplicación de matrices
    #print("Foward z")
    #print(z)
    a = red[l].activation(z)[0] # La función de activación retorna el valor activado y el derivado, necesitamos el activado para el forward
    #print("foward a")
    #print(a)
    out.append((z, a)) # Guardamos todas las combinaciones para poder usar la misma función en el backpropagation
  return out

def coste(tipo_pred, tipo_esp):
  return (np.mean((tipo_pred - tipo_esp) ** 2), (tipo_pred - tipo_esp)) 

def train(red, images, tipos, coste, learning_rate=0.0001):
  # forward 
  out = forward(red, images)
  # backward pass
  delta = []
  for i in reversed(range(0,len(red))):# recorrer hacie atrás del largo a 0
    z = out[i+1][0]
    a = out[i+1][1]
    #print("- a")
    #print(a)
    if i == len(red)-1:
        #delta última capa
        #print(a.shape)
        #print(tipos)
        x = coste(a, tipos)[1]
        #print("der. del coste:")
        #print(x)
        y = red[i].activation(a)[1]
        
        #print("der. de activación:")
        #print(y)
        delta.insert(0, x * y ) # delta 0 = derivada del coste (osea Ypred - Yesp) * derivada de activación de la capa
    else:
        # delta respecto al anterior
        delta_n = delta[0] @ aux_W.T * red[i].activation(a)[1]
        #print("--- delta n: ")
        #print(delta_n)
        delta.insert(0, delta_n) # delta n = delta(n+1) x W(n+1).T * derivada de activación de la capa 

    aux_W = red[i].W
    # Descenso del gradiente
    red[i].W = red[i].W - out[i][1].T @ delta[0] * learning_rate # nuevoW[i] = actualW[i] - salida[i].T x delta * learning_rate
    #break

  return out[-1][1]

topologia = [784, 4, 6, 4, 10]
red = crear_red(topologia, activation)
loss = []
pred = forward(red,images_train)
#print("* Prediccion Inicial")
#print(pred[-1][1])


#---------------------------------- APRENDIZAJE ---------------------------------#
time_start = time.time()
for i in range(50000): #1000
  #break
  p_tipos = train(red, images_train, tipos_train, coste, learning_rate=0.0005)
  if i % 25 == 0:
    costo = coste(p_tipos, tipos_train)[0]
    loss.append(costo)
  if (i == 0):
    costo = coste(p_tipos, tipos_train)[0]
    print("\n- Aprendizaje según coste de iteración -") #error cuadrático medio por cada tipo predicho
    print(f'Coste inicial: \n{costo}')
    print("\nAprendiendo... (esto puede tardar unos minutos)")
  if (i == 999):
    costo = coste(p_tipos, tipos_train)[0]
    print(f'\nCoste final: \n{costo}')

time_end = time.time()
print(f'-- Tiempo de aprendizaje: {time_end - time_start} (s)')

tp_1 = plt.subplot(1,1,1)
tp_1.plot(range(len(loss)), loss)
tp_1.set_title("Gráfica de Aprendizaje")
plt.show()

#------------------------------------ PRUEBAS -----------------------------------#

# 1. obtener tipos predichos y tipos esperados
tipos_pred = np.array(forward(red,images_test)[-1][1])
tipos_exp = np.array(tipos_test)

# 2. adaptar el formato
for i in range(len(tipos_pred)):
  tipos_pred[i] = np.array([1 if tipos_pred[i][j] == np.max(tipos_pred[i]) else 0 for j in range(len(tipos_pred[i]))])

print("Resultados esperados: ")
print(tipos_exp)
print("Resultados obtenidos: ")
print(tipos_pred)

# 3. calcular métricas de rendimiento
print(accuracy_score(tipos_exp, tipos_pred))
print(classification_report(tipos_exp, tipos_pred))

# 4. Generar matrices de confusión
matriz_confusion = multilabel_confusion_matrix(tipos_exp, tipos_pred)
clases = ['Polera', 'Pantalón', 'Sweater', 'Vestido', 'Saco', 'Sandalia', 'Camisa', 'Zapatilla', 'Bolso/Cartera', 'Bota']

for i, matrix in enumerate(matriz_confusion):
  labels = [f'True Neg\n{matrix[0][0]}',f'False Pos\n{matrix[0][1]}',f'False Neg\n{matrix[1][0]}',f'True Pos\n{matrix[1][1]}']

  labels = np.asarray(labels).reshape(2,2)

  ax = sns.heatmap(matriz_confusion[2], annot=labels, fmt='', cmap='rocket_r')

  ax.set_title(f'Matriz de Confusión para {clases[i]}\n\n');
  ax.set_xlabel('\nPredicted Values')
  ax.set_ylabel('Actual Values ');

  ## Ticket labels - List must be in alphabetical order
  ax.xaxis.set_ticklabels(['False','True'])
  ax.yaxis.set_ticklabels(['False','True'])

  ## Display the visualization of the Confusion Matrix.
  plt.show()



#dif = coste(tipos_pred[-1][1], tipos_test)[0]
#print(f"Coste Test {i}:")
#print(dif)
