""" hwcode.py
    Write the code for the HW exercises in this file.
"""
import json


def classify_tweets(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Classifies each tweet in jsonl_filename as either having positive
    or negative sentiment.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: A list of predictions (a list of strings "positive"
             or "negative") with a prediction for each tweet
    '''
    # Write code for exercise 2 part 1 here
    predictions = []
    return predictions

def most_negative_tweet(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Return the tweet that is the "most" negative - has the most negative words.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: The most negatives tweet text (string) 
    '''
    most_negative_tweet = ''
    # Write code for exercise 2 part 2 here.
    return most_negative_tweet
 
def most_positive_tweet(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    Return the tweet that is the "most" positive - has the most positive words.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: The most negatives tweet text (string) 
    '''
    # Write code for the exercise 2 part 2 here.
    most_positive_tweet = ''
    return most_positive_tweet
 
def most_negative_users(jsonl_filename, positive_lexicon, negative_lexicon, min_tweets):
    '''
    Return the 10 most negative users in the jsonl_filename dataset.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :param int min_tweets: The minimum number of tweets a user must have
                           to be considered the most positive.
    :return: A list of the 10 most negative users (screen names /strings)
             in the dataset.
    '''
    # Write code for the exercise 2 part 3 here.
    most_negative_users = ["a user"] * 10
    return most_negative_users

def most_positive_users(jsonl_filename, positive_lexicon, negative_lexicon, min_tweets):
    '''
    Return the 10 most positive users in the jsonl_filename dataset.

    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :param int min_tweets: The minimum number of tweets a user must have
                           to be considered the most positive.
    :return: A list of the 10 most positive users (screen names /strings)
             in the dataset.
    '''
    # Write code for the exercise 2 part 3 here.
    most_positive_users = ['a user'] * 10
    return most_positive_users

def most_negative_day(jsonl_filename, positive_lexicon, negative_lexicon):
    '''
    :param str jsonl_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
     :return: A string contain the day (MONTH DAY YEAR) with the largest proportion
              of negative tweets.
    '''
    most_negative_day = 'Oct 04 2017'
    return most_negative_day 
