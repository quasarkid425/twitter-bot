import tweepy
import praw
import os


def authenticate_twitter():
    # Authenticate with the Twitter API
    auth = tweepy.OAuth1UserHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
                                    os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
    return tweepy.API(auth)

def authenticate_reddit():
    # Authenticate with the Reddit API
    return praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"), client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                       username=os.getenv("REDDIT_USERNAME"), password=os.getenv("REDDIT_PASSWORD"), user_agent="my"
                                                                                                                "-app"
                                                                                                                "/1.0")
