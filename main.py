import time
import reddit_tweet as reddit


def main():
    while True:
        reddit.tweet_cat_content()
        time.sleep(25)


if __name__ == "__main__":
    main()
