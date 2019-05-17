# !/usr/bin/env python
# -*- coding: utf8 -*-

# Python 3.7.2

import unittest

from src.high_scoring_words import HighScoringWords

class TestHighScoringWords(unittest.TestCase):
    def setUp(self):
        self.score = HighScoringWords('test_word_list.txt')

    def test_initialises_properly(self):
        self.assertEqual(self.score.leaderboard, [])
        self.assertEqual(self.score.valid_words[0], 'aa')
        self.assertEqual(self.score.letter_values['a'], 1)

    def test_word_values(self):
        self.score.build_leaderboard_for_word_list()
        self.assertEqual(self.score.word_scores['aardvarks'], 17)

    def test_word_leaderboard_list(self):
        highest = self.score.build_leaderboard_for_word_list()
        self.assertEqual(highest[0], 'aardvarks')
        self.assertEqual(highest[1], 'aardwolves')

    def test_word_score_hash(self):
        self.score._create_word_score_hash(self.score.valid_words)
        self.assertEqual(self.score.word_scores['aardvarks'], 17)

    def test_does_not_exceed_max_leaderboard_limit(self):
        score_2 = HighScoringWords('wordlist.txt')
        top_100 = score_2.build_leaderboard_for_word_list()
        self.assertEqual(len(top_100), 100)
        self.assertEqual(top_100[0], 'razzamatazzes')
        self.assertEqual(top_100[-1], 'cyclohexylamines')

    def test_reverse_and_sort(self):
        self.score._create_word_score_hash(self.score.valid_words)
        highest_tuples = self.score._reverse_and_sort(self.score.word_scores)
        self.assertEqual(highest_tuples[0], ('aardvarks', 17))
        self.assertEqual(highest_tuples[1], ('aardwolves', 17))
