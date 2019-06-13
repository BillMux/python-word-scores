# !/usr/bin/env python
# -*- coding: utf8 -*-

# Python 3.7.2

import operator

class HighScoringWords:
    CHART_LENGTH = 100
    MIN_WORD_LENGTH = 3
    letter_values = {}

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values
        by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid
        words, one word per line
        :param lettervalues: a text file containing the score for each letter in
        the format letter:score one per line
        :return:
        """
        self.leaderboard = []
        self.word_scores = {}
        with open(validwords) as file:
            self.valid_words = file.read().splitlines()

        with open(lettervalues) as file:
            for line in file:
                key, val = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring
        CHART_LENGTH words from the complete set of valid words.
        :return:
        """
        self._create_word_score_dict(self.valid_words, self.word_scores)
        word_and_score = self._reverse_and_sort(self.word_scores)
        self.leaderboard = [i[0] for i in word_and_score][:self.CHART_LENGTH]
        return self.leaderboard

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that
        can be built using only the letters contained in the starting_letters
        string.
        The number of occurrences of a letter in the startingLetters String IS
        significant. If the starting letters are bulx, the word "bull" is NOT
        valid.
        There is only one l in the starting string but bull contains two l
        characters.
        Words are ordered in the leaderboard by their score (with the highest
        score first) and then alphabetically for words which have the same score
        :param starting_letters: a random string of letters from which to build
        words that are valid against the contents of the wordlist.txt file.
        :return:
        """
        words_of_starting_letters = []
        output = {}
        for word in self.valid_words:
            if word[:len(starting_letters)] == starting_letters:
                words_of_starting_letters.append(word)
                self._create_word_score_dict(words_of_starting_letters, output)
        tuples = self._reverse_and_sort(output)
        return [i[0] for i in tuples][:self.CHART_LENGTH]

    # private

    def _create_word_score_dict(self, valid, dictionary):
        """
        Creates a dictionary containing all valid words and their
        respective scores.
        """
        for word in valid:
            dictionary[word] = 0
            for letter in word:
                dictionary[word] += self.letter_values[letter]

    def _reverse_and_sort(self, scores):
        """
        Sorts the word-score dictionary in reverse order of score.
        Words of equal scores are sorted alphabetically.
        """
        return sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
