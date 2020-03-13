import tweepy
#Authentication twitter
auth=tweepy.OnAuthHandler("CONSUMER_KEY","CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN","ACCESS_TOKEN_SECRET")
#CREATE API object
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
timeline=api.home_timeline()
for tweet in timeline:
    printf(f"{tweet.user.name} said {tweet.txt}")
#home_timeline,a tweepy method,is used to get the last 20 entries in your timeline
#methods for tweets
api.update_status("test tweet from Tweepy python")
#methods for users
user=api.get_user("MikezGarcia")
print("user detials:")
print(user.name)
print(user.description)
print(user.location)
print("last 20 Followers:")
for follower in user.followers():
    print(follower.name)#get_user returns object contain user detials.
#methods for followers
 api.create_friendship("realpython")
 #create_friendship adds @reaipython to list of accounts you follow
 
