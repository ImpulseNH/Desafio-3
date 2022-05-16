import tensorflow as tf
import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from keras.engine import input_spec
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score, classification_report, multilabel_confusion_matrix, precision_score

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
images_train = (images_train - images_train.mean()) / images_train.std() + 0.000001
images_test = (images_test - images_test.mean()) / images_test.std() + 0.000001


modelo = Sequential()
modelo.add(Dense(4, input_dim=784, activation="sigmoid"))
modelo.add(Dense(6, activation="sigmoid"))
modelo.add(Dense(4, activation="sigmoid"))
modelo.add(Dense(10, activation="sigmoid"))

modelo.compile(loss='mse', optimizer='adam')

history = modelo.fit(images_train, tipos_train, epochs=100, batch_size=10, validation_split=0.1)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Función de coste')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


tipos_pred = modelo.predict(images_test)
tipos_exp = tipos_test.to_numpy()
for i in range(len(tipos_pred)):
  tipos_pred[i] = np.array([1 if tipos_pred[i][j] == np.max(tipos_pred[i]) else 0 for j in range(len(tipos_pred[i]))])
  

print(accuracy_score(tipos_exp, tipos_pred))
print(classification_report(tipos_exp, tipos_pred))

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