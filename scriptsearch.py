import tweepy
import textblob as tb
import json
from latlongfunc import latlong
import requests

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

#passing credentials to access twitter and assign it to api variable
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#in the future search_term will be an input
search_term = 'football'

#assigning all the relevant tweets to public_tweets
public_tweets = api.search(search_term)

#all of these print commands are just to see a read out in terminal to
#understand what the program is doing
print(search_term)

for tweet in public_tweets:
    #this is an analysis using a module called textblob
    analysis = tb.TextBlob(tweet.text)

    print(tweet.text)
    print(analysis.sentiment)
    #print(analysis.polarity)

    #it seems like there are four attributes that are relavent to mapping tweets
    #most in practice are null, user.location sometimes has something
    #but it is not necessary to use a real answer
    #"home sweet home" is hard to map :)

    # if tweet.coordinates != None:
    #     print('coordinates')
    #     print(tweet.coordinates)
    #     print(tweet.coordinates.coordinates)

    if tweet.user.location != None:
        print('user.location')
        print(tweet.user.location)
        try:
            print(latlong(tweet.user.location))
        except IndexError:
            print(tweet.user.location)

    # if tweet.geo != None:
    #     print('geo')
    #     print(tweet.geo)
    #     print(tweet.geo.coordinates)

    if tweet.place != None:
        print('place')
        print(tweet.place.full_name)
        print(tweet.place)
        try:
            print(latlong(tweet.place.full_name))
        except IndexError:
            print(tweet.place.full_name)
