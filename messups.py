import tweepy
import textblob
from textblob import TextBlob


consumer_key = "0XlgcKe6UTnXiSyikruP3upFw"
consumer_secret = "gwHgg8ds7idiEZrwuKtFrUQHEBUqI0VkEY0nZah46cjCTf5Shc"
access_token = "3890310195-DKYpqXORud5MOR2zicsscgAyCAH5K4NOUN6SEqJ"
access_secret =  "26yMtFG6bQudSF9svnAz0L4h7Ah5T2SmyJZ1Jx2Jt5pLx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

search_term = 'football'

public_tweets = api.search(search_term)

print search_term

for tweet in public_tweets:
    print tweet.text
    analysis = TextBlob(tweet.text)
    print analysis.sentiment
