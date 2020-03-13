timeline=api.home_timeline()
 for tweet in timeline:
     printf(f"{tweet.user.name} said {tweet.text}")
#methods for Tweets
api.update_status("test tweet from Tweepy python")
# in above line we have used update_status() to create a new tweet from a python string.
#methods for followers
api.create_friendship("realpython")
#it function adds @realpython to the list of accounts that you follow
#methods for your account
api.update_profile(description=" I like python")
#update_profile used to change our profile decription
#methods for likes
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)
#methods for blocking users
for block in api.blocks():
    print(block.name)
#this code iterates list of accounts you have blocked you gets block usres list.
#methods for searches
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
 #methods for trends list of current trends for any geographical location
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])
#methods for streaming
#1.The stream object uses the Twitter API to get tweets that match some criteria. This object is the source of tweets that are then processed by a stream listener.
#2.The stream listener receives tweets from the stream.


import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def _init_(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])

# models
# model classes are user,Status,Friendship,SearchResultas
#Suppose you want to fetch every tweet in which you are mentioned, and then mark each tweet as Liked and follow its author. You can do that like this:


tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favorite()
    tweet.user.follow()

 #cursors
for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print(f"{tweet.user.name} said: {tweet    
    


    
