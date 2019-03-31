""" hwcode.py
    Write the code for the HW exercises in this file.
"""

import json


def total_number_of_users(jsonl_filename):
    '''
    Returns the total number of tweets in jsonl_filename
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The total number (int) of tweets
    '''
    # Write code for exercise 1 here
    user_dict = dict()
    
    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip()) # Read 1 line at a time
        user_name = lineData["user"]["screen_name"]
        
        if user_name not in user_dict:
            user_dict[user_name] = 1
        else:
            user_dict[user_name] += 1
    
    myFile.close()

    total = len(user_dict)
    return total

def total_number_of_tweets(jsonl_filename):
    '''
    Returns the total number of tweets in jsonl_filename
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The total number (int) of tweets
    '''
    # Write code for exercise 1 here
    tweet_count = 0
    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip()) # Read 1 line at a time
        tweet_count += 1
    
    myFile.close()

    total = tweet_count
    return total

def average_tweets_per_user(jsonl_filename):
    '''
    Returns the average number of tweets per user
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The average number (float) of tweets tweeted by a user
    '''
    # Write code for exercise 2 here
    tweet_count = 0
    user_dict = dict()
    
    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip()) # Read 1 line at a time
        tweet_count += 1
        user_name = lineData["user"]["screen_name"]
        
        if user_name not in user_dict:
            user_dict[user_name] = 1
        else:
            user_dict[user_name] += 1
    
    myFile.close()

    average = tweet_count/len(user_dict)
    return average

def max_tweets_per_user(jsonl_filename):
    '''
    Returns the max number of tweets made by a user
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The max number (int) of tweets tweeted by a user
    '''
    user_dict = dict()
    
    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip()) # Read 1 line at a time
        
        user_name = lineData["user"]["screen_name"]
        
        if user_name not in user_dict:
            user_dict[user_name] = 1
        else:
            user_dict[user_name] += 1
    
    myFile.close()
    
    v=list(user_dict.values())
 
    max_tweets = max(v)
    return max_tweets

def user_with_most_tweets(jsonl_filename):
    '''
    Returns the user who made the most tweets
    :param str jsonl_filename: The file path of the twitter dataset
    :return: The screen_name (a string) of the user with the most tweets
    '''
    # Wrte code for exercise 3 here
    user_dict = dict()
    
    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip()) # Read 1 line at a time
        
        user_name = lineData["user"]["screen_name"]
        
        if user_name not in user_dict:
            user_dict[user_name] = 1
        else:
            user_dict[user_name] += 1
    
    myFile.close()
    
    v=list(user_dict.values())
    k=list(user_dict.keys())
 
    user_tweetsalot = k[v.index(max(v))]
    return user_tweetsalot

def dates_with_most_tweets(jsonl_filename):
    '''
    Returns a list of dates that had the most tweets.

    :param str jsonl_filename: The file path of the twitter dataset
    :return: A list of the 3 days (strings) with the most tweets
    '''
    # Write code for extra credit
    # Your code should return a list similar to the list below.
    create_date_dict = dict()
    
    myFile = open(jsonl_filename, encoding='utf-8')
    for line in myFile:
        lineData = json.loads(line.strip()) # Read 1 line at a time
        
        create_date = lineData["created_at"]
        day = create_date[4:10] + create_date[-5:]

        if day not in create_date_dict:
            create_date_dict[day] = 1
        else:
            create_date_dict[day] += 1

    myFile.close()   
    
    days_with_most_tweets =  sorted(create_date_dict, key=create_date_dict.get, reverse=True)[:3]
    #days_with_most_tweets = ['Oct 04 2017', 'Oct 05 2017', 'Oct 06 2017']
    return days_with_most_tweets 









