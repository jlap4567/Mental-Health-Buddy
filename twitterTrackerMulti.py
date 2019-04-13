import sys
import tweepy
import json
import threading 

consumer_key = "ehOAPbUM9ip4IVq2Iq8rLmy5e"
consumer_secret = "00MnazBUO5OY4Prxw0N3Yq88UiEP5QKuuqmAJqv3gN771hKstr"
access_key = "1061740751288262658-G3vwuy0iwzmS9IGdwiDi29jHah1Vfd"
access_secret = "XQgV0w0WJ5nfBVkib50OPPbTlBV6IQBJmqpXPaiEdlP16"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
file = open('today.txt', 'a')

#These are global variables that tract the current users
users = {}
threads = []

def trackMood(userName):
    """
    This function creates a stream to track a users current mood and handles the accordingly
    """
    return 0

def getOverAllMood(userName):
    """
    This function takes a string userName and gets the overall mood of a new 
    user based off of all of their last 200 posts as a double
    """
    return 0;

def handleTweet(userName):
    """
    This functions handles the tweets after
    """
    users[userName] = getOverAllMood()
    trackMood(userName)
    

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print (status.text)

    def on_data(self, data):
        json_data = json.loads(data)
        threads.append(threading.Thread(target=handleTweet, args=(json_data['user']['name'],))) 
        threads[-1].start()

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', str(status_code))
        return True # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['#TrackMyMood'])
