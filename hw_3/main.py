''' main.py
    Do NOT modify this file!
'''
from hwcode import *
import numpy as np

def main():
    # Exercise 1 and 2
    positive_words = set()
    negative_words = set()
    with open('./data/bing_liu/negative-words.txt', encoding="cp1252") as in_file:
        for row in in_file:
            negative_words.add(row.strip())
    with open('./data/bing_liu/positive-words.txt', encoding="cp1252") as in_file:
        for row in in_file:
            positive_words.add(row.strip())

    print("EXERCISE 1 and 2:")
    micro_f1 = classify_tweets_lexicon('./data/trainTwitterData.csv', positive_words, negative_words)
    try:
        assert(type(micro_f1) is float)
    except:
        print("ERROR: classify_tweets_lexicon should return an float")

    # Exercise 2
    micro_f1_svm = classify_tweets('./data/trainTwitterData.csv')
    try:
        assert(type(micro_f1_svm) is list)
    except:
        print("ERROR: classify should return an float")

    print("lexicon Test F1: {:.4f} SVM Val F1: {:.4f} SVM Test F1: {:.4f}".format(micro_f1, micro_f1_svm[0], micro_f1_svm[1]))

    print()
    print("Exercise 3:")
    words = predictive_words('./data/trainTwitterData.csv')
    try:
        assert(type(words) is np.ndarray or type(words) is list)
    except:
        print("ERROR: You should return a list of words for Exercise 3.")
    try:
        assert(len(words) == 10)
    except:
        print("ERROR: You should return a list of 10 words for Exercise 3.")

    print("Most predictive words:")
    for i, w in enumerate(words):
        print("Rank {} - {}".format(i+1, w))




    # Extra Credit 1
    print()
    print("EXTRA CREDIT:")
    better_micro_f1 = better_model('./data/trainTwitterData.csv')
    try:
        assert(type(better_micro_f1) is float)
    except:
        print("ERROR: better_model should return an float")
    try:
        assert(better_micro_f1 > micro_f1_svm[1])
    except:
        print("ERROR: You need to improve on Exercise 1 Part 2!")
    print("Exercise 2 F1: {:.4f} Extra Credit F1: {:.4f}".format(micro_f1_svm[1], better_micro_f1))

    print()
    print("EXTRA EXTRA CREDIT:")
    comp  = competition('./data/trainTwitterData.csv', './data/fakeTwitterTest.csv')
    try:
        assert(type(comp) is np.ndarray or type(comp) is list)
        print("Format looks okay for the competition. Good luck!")
    except:
        print("ERROR: competition should return a numpy array")


if __name__ == '__main__':
    main()
