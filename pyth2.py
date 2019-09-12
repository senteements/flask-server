import re
import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler


class TwitterClient(object):

    def __init__(self, CK, CS, AT, ATS):
        # print("Got this far.............{}".format(CK))
        consumer_key = CK
        consumer_secret = CS
        access_token = AT
        access_token_secret = ATS

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweets(self, query="peace", count="100"):
        tweets = []
        try:
            fetched_tweets = self.api.search(q=query, count=count)
            # print(*fetched_tweets)
            for tweet in fetched_tweets:
                parsed_tweet = {}
                if tweet.lang == "en":
                    parsed_tweet['text'] = self.clean_tweet(tweet.text)
                 #   print(parsed_tweet['text'])
                    if tweet.retweet_count > 0:
                        if parsed_tweet not in tweets:
                            tweets.append(parsed_tweet)
                    else:
                        tweets.append(parsed_tweet)
            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))


if __name__ == "__main__":
    api = TwitterClient()
    tweets = api.get_tweets(query='#vikram lander found', count=100)
    print(tweets)
