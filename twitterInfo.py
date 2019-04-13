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




def handleTweet(userName):
    tweets = {}
    for tweet in api.user_timeline(screen_name = userName, count = 200, include_rts = Flase):
        tweets[tweet['created_at']] = tweet['text']

    return tweets

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print (status.text)

    def on_data(self, data):
        json_data = json.loads(data)
        t1 = threading.Thread(target=handleTweet, args=(json_data['user']['name'],)) 
        t1.start()
        t1.join()

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', str(status_code))
        return True # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['#TrackMyMood'])
