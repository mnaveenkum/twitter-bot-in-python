#1.Using streams: to be notified when new content, such as tweets, that matches certain criteria is created
#2.Using polling: to periodically make Tweepy API calls and then check their results to see if they contain something new
#Presenting the Example Bots
#The Follow Followers Bot automatically follows anyone who follows you.
#The Fav & Retweet Bot automatically likes and retweets tweets that match certain criteria.
#The Reply to Mentions Bot automatically replies to tweets mentioning you that contain the words help or support.
# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
