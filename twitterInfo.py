import sys
import tweepy
import json
import threading 
import helper
import random

#Auth Keys (Don't push with these)
consumer_key = "Key"
consumer_secret = "Key"
access_key = "Key"
access_secret = "Key"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def handleTweet(userName):
    """
    This functions handles the tweets after it has
    been picked up by the listener
    """
    print(userName)
    tweets = []

    #gets a list of the last 50 tweets posted by a user
    for tweet in api.user_timeline(screen_name = userName, count = 50, include_rts = False, tweet_mode = 'extended'):
        tweets.append(tweet.full_text)
    print(tweets)

    #Creates a list of ways to destress
    stressIdeas = []
    file1 = open("./assets/waysToLowerStress.txt", 'r')
    for i in file1:
        stressIdeas.append(i)

    #Checks the mood of the user and returns the propper response
    if(helper.checkMood(tweets)):
        #helper.getGraph(tweets)
        message = "@" + userName + " We've notice that you've been more negative than usual lately we reccommend " + stressIdeas[random.randint(0,15)]
        api.update_with_media("foo.png", status=message)

    else:
        api.update_status(status = "You seem to be in a fine mood. Have a nice day")

class CustomStreamListener(tweepy.StreamListener):
    """
    Catches tweets in the stream and handles does the right thing with them
    """
    def on_status(self, status):
        print (status.text)

    def on_data(self, data):
        json_data = json.loads(data)
        t1 = threading.Thread(target=handleTweet, args=(json_data['user']['screen_name'],)) 
        t1.start()
        t1.join()

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', str(status_code))
        return True # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True # Don't kill the stream

#Create Twitter stream
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['#TrackMyMood'])
