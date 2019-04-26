#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key=uZw5RK8vQV0dincJi8baqNTNw,
consumer_secret=RyG0pF57mo1OvZNU14z5XhJanwBhPol1mHVUQuHlH8FH330e4h,
access_token=285201258-YamUyr4gxM19xKx6fEmEN2ESmqaNphgqbVLiLxza, 
access_token_secret=3FYUtkWN7oAWe71RUrnq1LVTsnjEYG18UEh6yR6roXb7s
)

user = "@YOUR_USERNAME"

auth = tweepy.OAuthHandler(keys[uZw5RK8vQV0dincJi8baqNTNw], keys[RyG0pF57mo1OvZNU14z5XhJanwBhPol1mHVUQuHlH8FH330e4h])
auth.set_access_token(keys[285201258-YamUyr4gxM19xKx6fEmEN2ESmqaNphgqbVLiLxza], keys[3FYUtkWN7oAWe71RUrnq1LVTsnjEYG18UEh6yR6roXb7s])
api = tweepy.API(auth)

def tweet():
	message=input("tweet: ")
	api.update_status(message)
	time.sleep(1000)
if __name__ == "__main__":
	while 1:
		tweet()
