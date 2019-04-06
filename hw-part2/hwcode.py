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

    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip())  # Read 1 line at a time
        tweet = lineData["full_text"]
        pos_sentiment = 0
        neg_sentiment = 0
        overall_sentiment = ''

        for word in tweet.lower().split():
            if word in (positive_lexicon):
                pos_sentiment += 1
            if word in (negative_lexicon):
                neg_sentiment += 1

        if pos_sentiment > neg_sentiment:
            overall_sentiment = "positive"
        elif neg_sentiment > pos_sentiment:
            overall_sentiment = "negative"
        else:
            overall_sentiment = "neutral"

        predictions.append(overall_sentiment)

    myFile.close()
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

    sentiment_values = []
    tweet_list = []

    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip())  # Read 1 line at a time
        tweet = lineData["full_text"]
        pos_sentiment = 0
        neg_sentiment = 0
        overall_sentiment = ''

        for word in tweet.lower().split():
            if word in (positive_lexicon):
                pos_sentiment += 1
            if word in (negative_lexicon):
                neg_sentiment += 1

        tweet_sentiment_value = pos_sentiment - neg_sentiment
        tweet_list.append(tweet)
        sentiment_values.append(tweet_sentiment_value)


    most_negative_tweet = tweet_list[sentiment_values.index(min(sentiment_values))]
    myFile.close()
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

    sentiment_values = []
    tweet_list = []

    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip())  # Read 1 line at a time
        tweet = lineData["full_text"]
        pos_sentiment = 0
        neg_sentiment = 0
        overall_sentiment = ''

        for word in tweet.lower().split():
            if word in (positive_lexicon):
                pos_sentiment += 1
            if word in (negative_lexicon):
                neg_sentiment += 1

        tweet_sentiment_value = pos_sentiment - neg_sentiment
        tweet_list.append(tweet)
        sentiment_values.append(tweet_sentiment_value)


    most_positive_tweet = tweet_list[sentiment_values.index(max(sentiment_values))]

    myFile.close()
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
    user_dict = dict()

    overall_sentiment = ''

    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        pos_sentiment = 0
        neg_sentiment = 0

        lineData = json.loads(line.strip())  # Read 1 line at a time

        user_name = lineData["user"]["screen_name"]
        tweet = lineData["full_text"]

        for word in tweet.lower().split():
            if word in (positive_lexicon):
                pos_sentiment += 1
            if word in (negative_lexicon):
                neg_sentiment += 1

        tweet_sentiment_value = pos_sentiment - neg_sentiment

        # add/update list of sentiment values in a list for each user
        if user_name not in user_dict:
            user_dict[user_name] = [tweet_sentiment_value]
        else:
            user_dict[user_name].append(tweet_sentiment_value)

    # create a new dict that has the user and average sentiment

    active_user_dict= dict()

    for name in user_dict:
        user_tweet_cnt = len(user_dict[name])
        if user_tweet_cnt >= min_tweets:
            active_user_dict[name] = sum(user_dict[name]) / user_tweet_cnt


    myFile.close()

    most_negative_users = sorted(active_user_dict, key=active_user_dict.get)[:10]

    #most_negative_users = ["a user"] * 10
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
    user_dict = dict()

    overall_sentiment = ''

    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        pos_sentiment = 0
        neg_sentiment = 0

        lineData = json.loads(line.strip())  # Read 1 line at a time

        user_name = lineData["user"]["screen_name"]
        tweet = lineData["full_text"]

        for word in tweet.lower().split():
            if word in (positive_lexicon):
                pos_sentiment += 1
            if word in (negative_lexicon):
                neg_sentiment += 1

        tweet_sentiment_value = pos_sentiment - neg_sentiment

        # add/update list of sentiment values in a list for each user
        if user_name not in user_dict:
            user_dict[user_name] = [tweet_sentiment_value]
        else:
            user_dict[user_name].append(tweet_sentiment_value)

    # create a new dict that has the user and average sentiment

    active_user_dict= dict()

    for name in user_dict:
        user_tweet_cnt = len(user_dict[name])
        if user_tweet_cnt >= min_tweets:
            active_user_dict[name] = sum(user_dict[name]) / user_tweet_cnt


    myFile.close()

    most_positive_users = sorted(active_user_dict, key=active_user_dict.get, reverse=True)[:10]
    #most_positive_users = ['a user'] * 10
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
    create_date_dict = dict()

    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        pos_sentiment = 0
        neg_sentiment = 0
        lineData = json.loads(line.strip())  # Read 1 line at a time

        create_date = lineData["created_at"]
        day = create_date[4:10] + create_date[-5:]
        tweet = lineData["full_text"]

        for word in tweet.lower().split():
            if word in (positive_lexicon):
                pos_sentiment += 1
            if word in (negative_lexicon):
                neg_sentiment += 1

        tweet_sentiment_value = pos_sentiment - neg_sentiment

        if day not in create_date_dict:
            create_date_dict[day] = [tweet_sentiment_value]
        else:
            create_date_dict[day].append(tweet_sentiment_value)

    sent_day_dict = dict()

    for tweet_date in create_date_dict:
        tweet_date_cnt = len(create_date_dict[tweet_date])
        day_neg_tweets = len([x for x in create_date_dict[tweet_date] if x < 0])
        sent_day_dict[tweet_date] = day_neg_tweets / tweet_date_cnt

    myFile.close()

    most_negative_day = sorted(sent_day_dict, key=sent_day_dict.get, reverse=True)[0]


    #most_negative_day = 'Oct 04 2017'
    return most_negative_day


