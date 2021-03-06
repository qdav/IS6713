""" hwcode.py
    Write the code for the HW exercises in this file.
"""

import csv
import numpy as np
import csv
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
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

    X = []  # Will be a list
    y = []  # will be a list
    with open(csv_filename) as inFile:
        iCSV = csv.reader(inFile, delimiter=',')
        next(iCSV)
        for row in iCSV:
            X.append(row[5])  # get tweet text
            y.append(row[0])  # get class
    X = np.array(X)  # convert to numpy array for scikit-learn
    y = np.array(y)  # convert to numpy array for scikit-learn
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    predictions = []

    for tweet in X_test:
        pos_sentiment = 0
        neg_sentiment = 0
        overall_sentiment = ''

        for word in tweet.lower().split():
            if word in (positive_lexicon):
                pos_sentiment += 1
            if word in (negative_lexicon):
                neg_sentiment += 1

        if pos_sentiment >= neg_sentiment:
            overall_sentiment = "positive"
        else:
            overall_sentiment = "negative"

        predictions.append(overall_sentiment)

    y_pred = np.array(predictions)
    inFile.close()
    f1_value = float(f1_score(y_test, y_pred, pos_label='positive'))

    return f1_value

def classify_tweets(csv_filename):
    '''
    Train a classifier and to predict sentiment on tweets.

    :param str csv_filename: The file path of the twitter dataset
    :return: A list of floats (GridSearchCV micro F1 and micro F1 score on test split)
    '''
    # Write code for exercise 1 part 2 here

    X = []  # Will be a list
    y = []  # will be a list
    with open(csv_filename) as inFile:
        iCSV = csv.reader(inFile, delimiter=',')
        next(iCSV)
        for row in iCSV:
            X.append(row[5])  # get tweet text
            y.append(row[0])  # get class
    X = np.array(X)  # convert to numpy array for scikit-learn
    y = np.array(y)  # convert to numpy array for scikit-learn
    # TODO: Remember to change the test size back to 0.2
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    vec = CountVectorizer(ngram_range = (1, 1), min_df = 1)
    cnt_stats = vec.fit(X_train)
    bow_train = vec.transform(X_train)

    params = {'C': [0.001, 0.01, 0.1, 1., 10.]}
    clf = GridSearchCV(LinearSVC(), params, cv=3, scoring="f1_micro")
    clf.fit(bow_train, y_train)

    train_best_score = clf.best_score_

    bow_test = vec.transform(X_test)
    y_pred = clf.predict(bow_test)

    test_score = float(f1_score(y_test, y_pred, pos_label='positive'))
    return [train_best_score, test_score]

def predictive_words(csv_filename):
    '''
    Train a classifier and to predict sentiment on tweets, then
    return the most predictive words.

    :param str csv_filename: The file path of the twitter dataset
    :return: A list of strings (words).
    '''
    # Write code for exercise 1 part 2 here

    X = []  # Will be a list
    y = []  # will be a list
    with open(csv_filename) as inFile:
        iCSV = csv.reader(inFile, delimiter=',')
        next(iCSV)
        for row in iCSV:
            X.append(row[5])  # get tweet text
            y.append(row[0])  # get class
    X = np.array(X)  # convert to numpy array for scikit-learn
    y = np.array(y)  # convert to numpy array for scikit-learn
    #TODO: Remember to change the test size back to 0.2
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

    vec = CountVectorizer(ngram_range = (1, 1), min_df = 1)
    cnt_stats = vec.fit(X_train)
    bow_train = vec.transform(X_train)

    # using best c-value from prior problem
    clf = LinearSVC(C=0.01, random_state=42)
    clf.fit(bow_train, y_train)
    coef_list = clf.coef_.transpose().tolist()
    top_pred_indicies = sorted(range(len(coef_list)), key=lambda i: coef_list[i], reverse=True)[:10]

    top_words = [vec.get_feature_names()[i] for i in top_pred_indicies]

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

