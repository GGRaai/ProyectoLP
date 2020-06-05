from tweet import *
from classifier import *
import matplotlib.pyplot as plt
import numpy as np


clf = SentimentClassifier()

t_positivos = []#Lista que almacena todos los tweets positivos
t_neutros = []#Lista que almacena los tweets neutros
t_negativos = []#Lista que almacena los tweets negativos
valores = {'Negativo':0,'Neutro':0,'Positivo':0}#Guarda los valores de cuantos tweets hay en cada categoria
total = 0

for trend in textos:
    for tweet in textos[trend]:
        a = clf.predict(tweet)

        total +=1
        if(a<0.3):
            t_negativos.append(tweet)
            valores['Negativo']+=1
        elif(a>0.5):
            t_positivos.append(tweet)
            valores['Positivo']+=1
        else:
            t_neutros.append(tweet)
            valores['Neutro']+=1

valores['Negativo'] = valores['Negativo']/total
valores['Neutro'] = valores['Neutro']/total
valores['Positivo'] = valores['Positivo']/total


objects = ('Negativo','Neutral','Positivo')
y_pos = np.arange(len(objects))
performance = [valores['Negativo'], valores['Neutro'], valores['Positivo']]
barlist=plt.bar(y_pos, performance, align='center', alpha=0.5)
barlist[0].set_color('red')
barlist[1].set_color('blue')
barlist[2].set_color('green')
plt.xticks(y_pos, objects)
plt.ylabel('Porcentaje')
plt.title('Analisis de sentimientos')
plt.show()
