import tweepy
from textblob import TextBlob
import csv
import operator
import numpy as np

#Step 1 - Authenticate
consumer_key = "Consumer Key"
consumer_secret = "Consumer Secret"

access_token = "Access Token"
access_token_secret = "Access Token Secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Paddy Jackson')

sentiment= ""
with open("data.csv", "w") as file:
	data = csv.writer(file)
	data.writerow(("Tweet", "Sentiment"))
	for tweet in public_tweets:
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		print (analysis)
		if analysis.sentiment.polarity > 0.1:
			sentiment = "Positive" 
		else:
			sentiment = "Negative"
		
		print(analysis.sentiment)
		data.writerow((tweet.text.encode('UTF-8'), sentiment))