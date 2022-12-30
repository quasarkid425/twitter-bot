import tweepy
import praw
import random
import requests
from io import BytesIO
from dotenv import load_dotenv
from auth import authenticate_twitter, authenticate_reddit

load_dotenv()

# List of subreddits for cat memes and videos
subreddit_list = ["catmemes", "catvideos", "funnycats", "catpictures", 'CatsInSinks', 'JellyBeanToes', 'CatsStandingUp',
                  'Kittens', 'CatsonGlass', 'TuckedInKitties', 'CatHighFive', 'CatCircles', 'Blep', 'CatReactionGifs',
                  'CatsvsTechnology', 'CatLoaf', 'MildlyStartledCats', 'Floof', 'Cats', 'CatsInBusinessAtt']


def tweet_cat_content():
    api = authenticate_twitter()
    reddit = authenticate_reddit()
    try:
        # Get a random subreddit from the list
        subreddit = random.choice(subreddit_list)
        # Get a random submission from the subreddit
        submission = random.choice(list(reddit.subreddit(subreddit).hot()))
        # Check if the submission is an image or a video
        if submission.url.endswith(".jpg") or submission.url.endswith(".png"):
            # Download the image and convert it to a BytesIO object
            image = BytesIO(requests.get(submission.url).content)
            # Upload the image to Twitter
            media = api.media_upload("cat.jpg", file=image)
            # Tweet the image, title, and author of the submission
            api.update_status(status=f"{submission.title} (by u/{submission.author})", media_ids=[media.media_id])
            print(f"Tweeted image: {submission.title}")
        elif submission.url.endswith(".mp4"):
            # Download the video and convert it to a BytesIO object
            video = BytesIO(requests.get(submission.url).content)
            # Upload the video to Twitter
            media = api.media_upload("cat.mp4", file=video, media_type="video/mp4")
            # Tweet the video, title, and author of the submission
            api.update_status(status=f"{submission.title} (by u/{submission.author})", media_ids=[media.media_id])
            print(f"Tweeted video: {submission.title}")
    except tweepy.TweepError as e:
        # Print the error message and skip the tweet if there is an error
        print(e)
        pass
    except praw.exceptions.APIException as e:
        # Print the error message and skip the tweet if there is an error
        print(e)
        pass
    except requests.exceptions.RequestException as e:
        # Print the error message and skip the tweet if there is an error
        print(e)
        pass
