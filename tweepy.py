import tweepy
#Authentication twitter
auth=tweepy.OnAuthHandler("CONSUMER_KEY","CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN","ACCESS_TOKEN_SECRET")
#CREATE API object
api=tweepy.API(auth)
# create a twwet
api.update_status("hello Tweepy")
