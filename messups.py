import tweepy
import textblob as tb
import json

# Load credentials into variables
"""
Let's store the credentials in a json object, that way we can reference that without having to hardcode
our twitter app credentials in the code :)
"""

with open('cred.json') as f:
    # Load the credentials file
    cred = json.load(f)
    # assign the objects to variables
    consumer_key = cred["consumer_key"]
    consumer_secret = cred["consumer_secret"]
    access_token = cred["access_token"]
    access_secret = cred["access_secret"]
#close the file
f.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

search_term = 'football'

public_tweets = api.search(search_term)

print(search_term)

for tweet in public_tweets:
    print(tweet.text)
    analysis = tb.TextBlob(tweet.text)
    print(analysis.sentiment)
    print(tweet.user.location)
    print(tweet.coordinates)
    print(tweet.geo)
    print(tweet.place)
