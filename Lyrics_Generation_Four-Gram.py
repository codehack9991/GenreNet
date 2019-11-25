#!/usr/bin/env python

import os
import io
import argparse
import string
import math
from random import randint

def get_word(wf):
    count = 0
    for key in wf:
        count += wf[key]
    rand = randint(1, count)
    for key in wf:
        if (rand <= wf[key]):
            return key
        else:
            rand -= wf[key]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--training_file', type=str, required=True)
    args = parser.parse_args()
    
    training_file = args.training_file
    text = []
    with io.open(training_file,'r',encoding='utf8') as f:
        text = f.read().lower().split(' ')

    # Count the words
    wordfreq = {}
    for i in range(0, len(text)-3):
        word1 = text[i]
        word2 = text[i+1]
        word3 = text[i+2]
        word4 = text[i+3]
        if word1 not in wordfreq:
            wordfreq[word1] = {}
        if word2 not in wordfreq[word1]:
            wordfreq[word1][word2] = {}
        if word3 not in wordfreq[word1][word2]:
            wordfreq[word1][word2][word3] = {}
        if word4 not in wordfreq[word1][word2][word3]:
            wordfreq[word1][word2][word3][word4] = 1
        else:
            wordfreq[word1][word2][word3][word4] += 1

    
    word1 = list(wordfreq.keys())[0]
    word2 = list(wordfreq[word1].keys())[0]
    word3 = list(wordfreq[word1][word2].keys())[0]
    sentence = "%s %s %s " % (word1, word2, word3)
    for i in range(0,200):
        word4 = get_word(wordfreq[word1][word2][word3])
        sentence += word4 + " ";
        word1 = word2
        word2 = word3
        word3 = word4

    print(sentence)

if __name__ == "__main__":
    main()
