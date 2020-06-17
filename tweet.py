import tweepy
import time

#Access keys
file = open('data.txt','r') #archivo con credenciales
data={}
#crea un diccionario con llaves que necesitamos para ingresar a la API
for line in file:
    (x,y) = line.strip().split('=')
    data[x] = y
file.close()
woeid = 349859 #Id para chile en twitter

auth = tweepy.OAuthHandler(data['api_key'],data['api_secret'])
auth.set_access_token(data['access_token'],data['access_token_secret'])#Meterse a twitter


api = tweepy.API(auth)
fechas_tweets = []
fechas = dict()
textos_tweets = []
textos = dict()
trends1 = api.trends_place(woeid)#conseguir trends de chile
trends = list([trend for trend in trends1[0]['trends']])#Conseguir los nombres de las trends

for trend in trends:
    q = trend['name']
    tweets = tweepy.Cursor(api.search,q=q,result_type="mixed").items(10)

    for tweet in tweets:
        fechas_tweets.append(str(tweet.created_at))#Agrega a una lista con todas las fechas
        textos_tweets.append(tweet.text)#Agrega a una lista con los textos

    fechas.update({q:fechas_tweets})#Crea un diccionario para cada trend (trend:fechas)
    fechas_tweets = []#Vuelve a vacia la lista, para asi tener una distinta por cada trend
    textos.update({q:textos_tweets})
    textos_tweets = []
    #time.sleep(30)
