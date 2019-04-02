''' main.py
    Do NOT modify this file!
'''
from hwcode import *

def main():
    print("EXERCISE 1:")
    positive_words = set()
    negative_words = set()
    with open('./data/bing_liu/negative-words.txt', encoding="cp1252") as in_file:
        for row in in_file:
            negative_words.add(row.strip())
    with open('./data/bing_liu/positive-words.txt', encoding="cp1252") as in_file:
        for row in in_file:
            positive_words.add(row.strip())

    predictions = classify_tweets('./data/data.jsonl', positive_words, negative_words) 
    try:
        assert(type(predictions) is list)
    except:
        print("ERROR: classify_tweets should return a list")
    print("Number of predicted positive tweets: {}".format(predictions.count("positive")))
    print("Number of predicted negative tweets: {}".format(predictions.count("negative")))
    print("Number of predicted neutral tweets: {}".format(predictions.count("neutral")))

    # Exercise 2
    print()
    print("EXERCISE 2:")
    negative_tweet = most_negative_tweet('./data/data.jsonl', positive_words, negative_words) 
    try:
        assert(type(negative_tweet) is str)
    except:
        print("ERROR: most_negative_tweet should return a string")
    print("The most negative tweet: {}".format(negative_tweet))

    positive_tweet = most_positive_tweet('./data/data.jsonl', positive_words, negative_words) 
    try:
        assert(type(positive_tweet) is str)
    except:
        print("ERROR: most_positive_tweet should return an string")
    print("The most positive tweet: {}".format(positive_tweet))
    print()

    print("EXERCISE 3:")
    one_neg_users = most_negative_users('./data/data.jsonl', positive_words, negative_words, 1)
    try:
        assert(type(one_neg_users) is list)
    except:
        print("ERROR: most_negative_users should return a list")

    try:
        assert(len(one_neg_users) == 10)
    except:
        print("ERROR: most_negative_users should return a list of length 10")

    print("The most negative users that tweeted at least once:")
    for i,screen_name in enumerate(one_neg_users):
        print("{0}: {1}".format(i,screen_name))
    print()

    five_neg_users = most_negative_users('./data/data.jsonl', positive_words, negative_words, 5)
    try:
        assert(type(five_neg_users) is list)
    except:
        print("ERROR: most_negative_users should return a list")

    try:
        assert(len(five_neg_users) == 10)
    except:
        print("ERROR: most_negative_users should return a list of length 10")
    print("The most negative users that tweeted at least five times:")
    for i,screen_name in enumerate(five_neg_users):
        print("{0}: {1}".format(i,screen_name))
    print()

    one_pos_users = most_positive_users('./data/data.jsonl', positive_words, negative_words, 1)
    try:
        assert(type(one_pos_users) is list)
    except:
        print("ERROR: most_positive_users should return a list")

    try:
        assert(len(one_pos_users) == 10)
    except:
        print("ERROR: most_positive_users should return a list of length 10")

    print("The most positive users that tweeted at least once:")
    for i,screen_name in enumerate(one_pos_users):
        print("{0}: {1}".format(i,screen_name))
    print()

    five_pos_users = most_positive_users('./data/data.jsonl', positive_words, negative_words, 5)
    try:
        assert(type(five_pos_users) is list)
    except:
        print("ERROR: most_positive_users should return a list")
    try:
        assert(len(five_pos_users) == 10)
    except:
        print("ERROR: most_positive_users should return a list of length 10")
    print("The most positive users that tweeted at least five times:")
    for i,screen_name in enumerate(five_pos_users):
        print("{0}: {1}".format(i,screen_name))
    print()

    # Extra Credit
    print("EXTRA CREDIT")
    neg_day = most_negative_day('./data/data.jsonl', positive_words, negative_words) 
    try:
        assert(type(neg_day) is str)
    except:
        print("ERROR: most_negative_day should return a string")
    print("The most negative day: {}".format(neg_day))


if __name__ == '__main__':
    main()
