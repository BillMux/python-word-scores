# !/usr/bin/env python
# -*- coding: utf8 -*-

# Python 3.7.2

__author__ = 'codesse'

import operator

class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    # valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.leaderboard = [] # initialise an empty leaderboard
        self.word_scores = {}
        with open(validwords) as file:
            self.valid_words = file.read().splitlines()

        with open(lettervalues) as file:
            for line in file:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring
        MAX_LEADERBOARD_LENGTH words from the complete set of valid words.
        :return:
        """
        self._create_word_score_hash(self.valid_words)
        word_score_tuples = self._reverse_and_sort(self.word_scores)
        self.leaderboard = [i[0] for i in word_score_tuples]
        return self.leaderboard



    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return:
        """

    # private

    def _create_word_score_hash(self, valid):
        for word in valid:
            self.word_scores[word] = 0
            for letter in word:
                self.word_scores[word] += self.letter_values[letter]

    def _reverse_and_sort(self, scores):
        return sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
