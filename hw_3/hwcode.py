""" hwcode.py
    Write the code for the HW exercises in this file.
"""

import csv
import numpy as np
# Add any extra imports you want here

def classify_tweets_lexicon(csv_filename, positive_lexicon, negative_lexicon):
    '''
    Classifies each tweet in the test split of csv_filename as
    either having positive or negative sentiment.

    :param str csv_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: A float (micro F1 score on test split)
    '''
    # Write code for exercise 1 part 1 here
    return 0.0

def classify_tweets(csv_filename):
    '''
    Train a classifier and to predict sentiment on tweets.

    :param str csv_filename: The file path of the twitter dataset
    :return: A list of floats (GridSearchCV micro F1 and micro F1 score on test split)
    '''
    # Write code for exercise 1 part 2 here
    gridCV_best_score = 0.3
    test_score = 0.2
    return [gridCV_best_score, test_score]

def predictive_words(csv_filename):
    '''
    Train a classifier and to predict sentiment on tweets, then
    return the most predictive words.

    :param str csv_filename: The file path of the twitter dataset
    :return: A list of strings (words).
    '''
    # Write code for exercise 1 part 2 here
    top_words = ['best', 'great', 'awesome', 'love', 'good',
                 'cool', 'happy', 'happily', 'lovely', 'fun']
    return top_words



def better_model(csv_filename):
    '''
    Train a classifier and to predict sentiment on tweets.

    :param str csv_filename: The file path of the twitter dataset
    :return: A float (micro F1 score on test split)
    '''
    # Write code for exercise 1 part 2 here
    return 0.4

def competition(csv_train_filename, csv_test_filename):
    '''
    Train a classifier and to predict sentiment on tweets.

    :param str csv_train_filename: The train data file path of the twitter dataset
    :param str csv_test_filename: The test data  file path of the twitter dataset
    :return: A np.ndarray The output of clf.predict()
    '''
    # Write code for exercise 1 part 2 here
    return np.array(["positive","negative"])

