from tweet import *
from classifier import SentimentClassifier
import matplotlib.pyplot as plt
import numpy as np


clf = SentimentClassifier()

t_positivos = []#Lista que almacena todos los tweets positivos
t_neutros = []#Lista que almacena los tweets neutros
t_negativos = []#Lista que almacena los tweets negativos
valores = {'Negativo':0,'Neutro':0,'Positivo':0}#Guarda los valores de cuantos tweets hay en cada categoria
valores_n = {'Negativo':0,'Neutro':0,'Positivo':0}#Guarda los valores de cuantas noticias hay en cada categoria
total = 0
total_n = 0
totales = {'Negativo':0,'Neutro':0,'Positivo':0}
totales_n = {'Negativo':0,'Neutro':0,'Positivo':0}


def sacar_valores():
    global total
    global valores
    global totales
    t_neutros = [tweet for trend in textos for tweet in textos[trend] if clf.predict(tweet)<=0.5 and clf.predict(tweet)>=0.1]
    t_negativos = [tweet for trend in textos for tweet in textos[trend] if clf.predict(tweet)<0.1]
    t_positivos = [tweet for trend in textos for tweet in textos[trend] if clf.predict(tweet)>0.5]
    totales['Neutro'] = valores["Neutro"] = len(t_neutros)
    totales['Positivo'] = valores["Positivo"] = len(t_positivos)
    totales['Negativo'] = valores["Negativo"] = len(t_negativos)
    total = len(t_neutros)+len(t_positivos)+len(t_negativos)
    valores['Negativo'] = valores['Negativo']/total
    valores['Neutro'] = valores['Neutro']/total
    valores['Positivo'] = valores['Positivo']/total
    print(valores)
    print(totales)
    print(total)

def sacar_valores_noticias(lista):
    global total_n
    global valores_n
    global totales_n
    valores_n['Neutro'] = totales_n['Neutro'] = len([cuerpo for noticia in lista for cuerpo in noticia.cuerpo if clf.predict(cuerpo)<=0.5 and clf.predict(cuerpo)>=0.1])
    valores_n['Positivo'] = totales_n['Positivo'] = len([cuerpo for noticia in lista for cuerpo in noticia.cuerpo if clf.predict(cuerpo)>0.5])
    valores_n['Negativo'] = totales_n['Negativo'] = len([cuerpo for noticia in lista for cuerpo in noticia.cuerpo if clf.predict(cuerpo)<0.1])
    total_n = valores_n['Neutro'] + valores_n['Positivo'] + valores_n['Negativo']
    valores_n['Negativo'] = valores_n['Negativo']/total_n
    valores_n['Neutro'] = valores_n['Neutro']/total_n
    valores_n['Positivo'] = valores_n['Positivo']/total_n
    print(valores_n)
    print(totales_n)
    print(total_n)


def graficos():
    global valores
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

def graficos_n():
    global valores_n
    objects = ('Negativo','Neutral','Positivo')
    y_pos = np.arange(len(objects))
    performance = [valores_n['Negativo'], valores_n['Neutro'], valores_n['Positivo']]
    barlist=plt.bar(y_pos, performance, align='center', alpha=0.5)
    barlist[0].set_color('red')
    barlist[1].set_color('blue')
    barlist[2].set_color('green')
    plt.xticks(y_pos, objects)
    plt.ylabel('Porcentaje')
    plt.title('Analisis de sentimientos noticias')
    plt.show()
