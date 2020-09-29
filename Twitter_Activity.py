import tweepy
import numpy as np
from textblob import TextBl

## set up key ##
## I never got developer access to finish review of my account ##
consumer_key = 'paste consumer key'
consumer_secret = 'paste consumer secret'

access_token = 'paste access token'
access_token_secret = 'past access token secret'

## authentication##
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


def tweet_analysis(query):
    tweets = tweepy.Cursor(api.search, q=query + " -filter:retweets").items(20)

    subjectivities = []
    polarities = []

    for tweet in tweets:
        phrase = TextBlob(tweet.text)

        if not is_english(phrase):
            phrase = TextBlob(str(phrase.translate(to='en')))

        if phrase.sentiment.polarity != 0.0 and phrase.sentiment.subjectivity != 0.0:
            polarities.append(phrase.sentiment.polarity)
            subjectivities.append(phrase.sentiment.subjectivity)

        print('tweet: ' + tweet.text)
        print('polarity: ' + str(phrase.sentiment.polarity))
        print('subjectivity: ' + str(phrase.sentiment.subjectivity))
        print('..................')

    return {'polarity': polarities, 'subjectivity': subjectivities}


def is_english(text):
    if text.detect_language() == 'en':
        return True
    return False


def get_polarity_mean(valid_tweets):
    return np.mean(valid_tweets['polarity'])


def get_weighted_polarity_mean(valid_tweets):
    return np.average(valid_tweets['polarity'],weights=valid_tweets['subjectivity'])


def print_result(mean):
    if mean > 0.0:
        print('POSITIVE')
    elif mean == 0.0:
        print('NEUTRAL')
    else:
        print('NEGATIVE')


if __name__ == "__main__":
    query = input("Enter a query to find: ")
    analysis = tweet_analysis(query)

    print('WEIGHTED MEAN: ' + str(get_polarity_mean(analysis)))
    print_result(get_weighted_polarity_mean(analysis))

    print('MEAN: ' + str(get_polarity_mean(analysis)))
    print_result(get_polarity_mean(analysis))