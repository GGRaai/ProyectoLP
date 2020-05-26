import tweepy


#Access keys
file = open('data.txt','r')
data={}
for line in file:
    (x,y) = line.strip().split('=')
    data[x] = y
file.close()
woeid = 349859 #Id para chile en twitter

auth = tweepy.OAuthHandler(data['api_key'],data['api_secret'])
auth.set_access_token(data['access_token'],data['access_token_secret'])#Meterse a twitter

api = tweepy.API(auth)
trends1 = api.trends_place(woeid)#conseguir trends de chile

trends = list([trend['name'] for trend in trends1[0]['trends']])#Conseguir los nombres de las trends
print(trends)
