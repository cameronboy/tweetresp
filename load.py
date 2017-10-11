import tweepy
from tweepy import OAuthHandler

consumer_key = "0XlgcKe6UTnXiSyikruP3upFw"
consumer_secret = "gwHgg8ds7idiEZrwuKtFrUQHEBUqI0VkEY0nZah46cjCTf5Shc"
access_token = "3890310195-DKYpqXORud5MOR2zicsscgAyCAH5K4NOUN6SEqJ"
access_secret =  "26yMtFG6bQudSF9svnAz0L4h7Ah5T2SmyJZ1Jx2Jt5pLx"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
