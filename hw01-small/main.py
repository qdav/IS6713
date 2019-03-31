''' main.py
    Do NOT modify this file!
'''
from hwcode import *

def main():

    print("Homework 1:")
    # Exercise 1
    total_users = total_number_of_users('./data/data.jsonl')
    try:
        assert(type(total_users) is int or type(total_users) is float)
    except:
        print("ERROR: total_number_of_users should return an int")

    print("The dataset has {} users".format(total_users))

    total_tweets = total_number_of_tweets('./data/data.jsonl')
    try:
        assert(type(total_tweets) is int or type(total_tweets) is float)
    except:
        print("ERROR: total_number_of_tweets should return an int")
    print("The dataset has {} tweets".format(total_tweets))

    # Exercise 2

    avg_tweets_p_user = average_tweets_per_user('./data/data.jsonl')
    try:
        assert(type(avg_tweets_p_user) is float)
    except:
        print("ERROR: average_tweets_per_user should return a float")
    print("The dataset has an average of {0:.2f} tweets per user".format(avg_tweets_p_user))

    max_tweets_p_user = max_tweets_per_user('./data/data.jsonl')
    try:
        assert(type(max_tweets_p_user) is int or type(max_tweets_p_user) is float)
    except:
        print("ERROR: max_tweets_per_user should return an int")
    print("The user with the most tweets has {} tweets".format(max_tweets_p_user))

    # Exercise 3

    most_tweets_user = user_with_most_tweets('./data/data.jsonl')
    try:
        assert(type(most_tweets_user) is str)
    except:
        print("ERROR: user_with_most_tweets should return a string")
    print("The user with the most tweets is {}".format(most_tweets_user))
    print()

    # Extra Credit
    print("EXTRA CREDIT")
    days_most = dates_with_most_tweets('./data/data.jsonl')
    try:
        assert(type(days_most) is list)
    except:
        print("ERROR: days_with_most_tweets should return a list")
    try:
        assert(len(days_most) == 3)
    except:
        print("ERROR: dates_with_most_tweets should return a list of length 10")
    print("The dates with the most tweets:")
    for i,date in enumerate(days_most):
        print("{0}: {1}".format(i,date))


if __name__ == '__main__':
    main()
