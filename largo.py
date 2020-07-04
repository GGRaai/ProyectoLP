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
    l_corto_emol = [i for i in count_emol if i<400]
    l_medio_emol = [i for i in count_emol if i>= 400 and i<800]
    l_largo_emol = [i for i in count_emol if i>= 800]
    valores_emol = {'Corto': len(l_corto_emol), 'Medio': len(l_medio_emol), 'Largo': len(l_largo_emol)}
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

    l_corto_lt = [i for i in count_lt if i < 400]
    l_medio_lt = [i for i in count_lt if i >= 400 and i < 800]
    l_largo_lt = [i for i in count_lt if i >= 800]
    valores_lt = {'Corto': len(l_corto_lt), 'Medio': len(l_medio_lt), 'Largo': len(l_largo_lt)}
    y_pos = np.arange(len(objects))
    performance = [valores_lt['Corto'], valores_lt['Medio'], valores_lt['Largo']]
    barlist=plt.bar(y_pos, performance, align='center', alpha=0.5)
    barlist[0].set_color('red')
    barlist[1].set_color('blue')
    barlist[2].set_color('green')
    plt.xticks(y_pos, objects)
    plt.title('Largo Noticias La Tercera')
    plt.show()

    count_tweets = []
    for trend,cuerpos in textos.items():
        for tweet in cuerpos:
            largo = tweet.count(" ")+1
            count_tweets.append(largo)
    l_corto_tweet = [i for i in count_tweets if i <15]
    l_medio_tweet = [i for i in count_tweets if i>=15 and i<24]
    l_largo_tweet = [i for i in count_tweets if i>=24]
    valores_tweet = {'Corto': len(l_corto_tweet), 'Medio': len(l_medio_tweet), 'Largo': len(l_largo_tweet)}
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
