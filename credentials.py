import tweepy
import time

CONSUMER_KEY = 'YOUR CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR CONSUMER_SECRET KEY'
ACCESS_KEY = 'YOUR ACCESS_KEY'
ACCESS_SECRET = 'YOUR ACCESS_SECRET KEY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
