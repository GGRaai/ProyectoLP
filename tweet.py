import tweepy


#Access keys
api_key = 'gD7F2G8L8d8UKjxDeV2pryVHG'
api_secret = 'G9es9zb6GTAmWsLyS1tqSlpvXr5QCIKWZ52IC2ill26zu5IEdQ'
access_token = '328254791-2QPxN1KmDjfa2mIoTC5RUkkbt3M5xEvF2P8X2ISE'
access_token_secret = '6uVBm9bMeax3mq4vZ3TzMDf4dcQeDMaBFC3XgR9jIJ6de'
woeid = 349859 #Id para chile en twitter

auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_token_secret)#Meterse a twitter

api = tweepy.API(auth)
trends1 = api.trends_place(woeid)#conseguir trends de chile

trends = list([trend['name'] for trend in trends1[0]['trends']])#Conseguir los nombres de las trends
print(trends)
