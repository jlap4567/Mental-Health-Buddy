import tweepy

consumer_key = "ehOAPbUM9ip4IVq2Iq8rLmy5e"
consumer_secret = "00MnazBUO5OY4Prxw0N3Yq88UiEP5QKuuqmAJqv3gN771hKstr"
access_token = "1061740751288262658-G3vwuy0iwzmS9IGdwiDi29jHah1Vfd"
access_token_secret = "XQgV0w0WJ5nfBVkib50OPPbTlBV6IQBJmqpXPaiEdlP16"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
