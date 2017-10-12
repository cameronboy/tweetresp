import tweepy
import json


# Load credentials into variables
with open('cred.json') as f:
    cred = json.load(f)
    consumer_key = cred["consumer_key"]
    consumer_secret = cred["consumer_secret"]
    access_token = cred["access_token"]
    access_secret = cred["access_secret"]
f.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
