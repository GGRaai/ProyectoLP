from tweet import *
import noticias
import numpy as np
import matplotlib.pyplot as plt

def largo(objetos):
    count_emol = []
    count_lt = []
    for noticia in objetos:
        if(noticia.cuerpo!=[]):
            cont=0
            for p in noticia.cuerpo:
                cont+=p.count(" ")+1
            if(type(noticia) is noticias.Emol):
                count_emol.append(cont)
            else:
                count_lt.append(cont)

    valores_emol = {'Corto':0,'Medio':0,'Largo':0}
    for i in count_emol:
        if(i<400):
            valores_emol['Corto']+=1
        if(i>=400 and i<2000):
            valores_emol['Medio']+=1
        else:
            valores_emol['Largo']+=1
    objects = ('Corto','Medio','Largo')
    y_pos = np.arange(len(objects))
    performance = [valores_emol['Corto'], valores_emol['Medio'], valores_emol['Largo']]
    barlist=plt.bar(y_pos, performance, align='center', alpha=0.5)
    barlist[0].set_color('red')
    barlist[1].set_color('blue')
    barlist[2].set_color('green')
    plt.xticks(y_pos, objects)
    plt.title('Largo Noticias Emol')
    plt.show()
    valores_lt = {'Corto':0,'Medio':0,'Largo':0}
    for i in count_lt:
        if(i<400):
            valores_lt['Corto']+=1
        if(i>=400 and i<2000):
            valores_lt['Medio']+=1
        else:
            valores_lt['Largo']+=1
    objects = ('Corto','Medio','Largo')
    y_pos = np.arange(len(objects))
    performance = [valores_lt['Corto'], valores_lt['Medio'], valores_lt['Largo']]
    barlist=plt.bar(y_pos, performance, align='center', alpha=0.5)
    barlist[0].set_color('red')
    barlist[1].set_color('blue')
    barlist[2].set_color('green')
    plt.xticks(y_pos, objects)
    plt.title('Largo Noticias La Tercera')
    plt.show()

    valores_tweet = {'Corto':0,'Medio':0,'Largo':0}
    count_tweets = []
    for trend,cuerpos in textos.items():
        for tweet in cuerpos:
            largo = tweet.count(" ")+1
            count_tweets.append(largo)
    for i in count_tweets:
        if(i<15):
            valores_tweet['Corto']+=1
        if(i>=15 and i<24):
            valores_tweet['Medio']+=1
        else:
            valores_tweet['Largo']+=1
    objects = ('Corto','Medio','Largo')
    y_pos = np.arange(len(objects))
    performance = [valores_tweet['Corto'], valores_tweet['Medio'], valores_tweet['Largo']]
    barlist=plt.bar(y_pos, performance, align='center', alpha=0.5)
    barlist[0].set_color('red')
    barlist[1].set_color('blue')
    barlist[2].set_color('green')
    plt.xticks(y_pos, objects)
    plt.title('Largo Tweets')
    plt.show()
