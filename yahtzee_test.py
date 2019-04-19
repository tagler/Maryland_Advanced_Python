#!/usr/bin/env python

import unittest
from yahtzee import Roll, Type
import yahtzee
from os import system


class TestYahtzee(unittest.TestCase):
    def testAuthor(self):
        '''Module docstring MUST CONTAIN your first name + last initital'''
        self.assertLess(4, len(yahtzee.__doc__))

    def testAces(self):
        '''Score only 1s rolled'''
        self.assertEqual( 1, Roll(4, 3, 5, 2, 1).aces)
        self.assertEqual( 5, Roll(1, 1, 1, 1, 1).aces)

    def testTwos(self):
        '''Score only 2s rolled'''
        self.assertEqual( 2, Roll(4, 3, 5, 2, 1).twos)
        self.assertEqual( 6, Roll(2, 1, 2, 1, 2).twos)

    def testThrees(self):
        '''Score only 3s rolled'''
        self.assertEqual( 3, Roll(4, 3, 5, 2, 1).threes)
        self.assertEqual( 0, Roll(2, 1, 2, 1, 2).threes)

    def testFours(self):
        '''Score only 4s rolled'''
        self.assertEqual( 4, Roll(4, 3, 5, 2, 1).fours)
        self.assertEqual( 8, Roll(2, 4, 2, 4, 2).fours)

    def testFives(self):
        '''Score only 5s rolled'''
        self.assertEqual( 5, Roll(4, 3, 5, 2, 1).fives)
        self.assertEqual(15, Roll(5, 5, 2, 4, 5).fives)

    def testSixes(self):
        '''Score only 6s rolled'''
        self.assertEqual( 0, Roll(4, 3, 5, 2, 1).sixes)
        self.assertEqual(12, Roll(6, 5, 2, 6, 5).sixes)

    def testThreeOfAKind(self):
        '''3-of-a-kind scores the sum of all dice'''
        self.assertEqual( 0, Roll(4, 3, 5, 4, 1).three_of_a_kind)
        self.assertEqual(23, Roll(5, 5, 2, 6, 5).three_of_a_kind)

    def testFourOfAKind(self):
        '''4-of-a-kind scores the sum of all dice'''
        self.assertEqual( 9, Roll(1, 1, 5, 1, 1).four_of_a_kind)
        self.assertEqual( 0, Roll(5, 5, 2, 2, 5).four_of_a_kind)

    def testFullHouse(self):
        '''Three of one, two of another scores 25'''
        self.assertEqual( 0, Roll(1, 1, 5, 1, 1).full_house)
        self.assertEqual(25, Roll(5, 5, 2, 2, 5).full_house)

    def testSmallStraight(self):
        '''4-in-a-row scores 30'''
        self.assertEqual(30, Roll(4, 3, 5, 1, 6).small_straight)
        self.assertEqual( 0, Roll(5, 5, 2, 2, 5).small_straight)
        self.assertEqual(30, Roll(4, 3, 5, 2, 6).small_straight)

    def testLargeStraight(self):
        '''5-in-a-row scores 40'''
        self.assertEqual(40, Roll(4, 3, 5, 2, 6).large_straight)
        self.assertEqual( 0, Roll(5, 5, 2, 2, 5).large_straight)
        self.assertEqual( 0, Roll(4, 3, 5, 1, 6).large_straight)

    def testYahtzee(self):
        '''5-of-a-kind scores 50'''
        self.assertEqual(50, Roll(4, 4, 4, 4, 4).yahtzee)
        self.assertEqual( 0, Roll(5, 5, 2, 2, 5).yahtzee)

    def testChance(self):
        '''Scores the sum of all dice'''
        self.assertEqual(15, Roll(4, 3, 5, 2, 1).chance)
        self.assertEqual( 5, Roll(1, 1, 1, 1, 1).chance)

    def testScoreAs(self):
        '''Scores the roll as the specified opportunity'''
        self.assertEqual( 5, Roll(1, 1, 1, 1, 1).score_as(Type.ACES))
        self.assertEqual( 5, Roll(1, 1, 1, 1, 1).score_as(Type.CHANCE))
        self.assertEqual( 5, Roll(1, 1, 1, 1, 1).score_as(Type.FOUR_OF_A_KIND))
        self.assertEqual(50, Roll(1, 1, 1, 1, 1).score_as(Type.YAHTZEE))
        self.assertEqual( 0, Roll(1, 1, 1, 1, 1).score_as(Type.THREES))
        self.assertEqual( 0, Roll(1, 1, 2, 1, 1).score_as(Type.YAHTZEE))
        self.assertEqual(30, Roll(3, 4, 5, 1, 6).score_as(Type.SMALL_STRAIGHT))
        self.assertEqual(19, Roll(3, 4, 5, 1, 6).score_as(Type.CHANCE))

    def testFindUpperBest(self):
        '''Finds best scoring opportunity from upper part of scorepad'''
        self.assertEqual(Type.SIXES,  Roll(1, 6, 1, 2, 3).best_upper)
        self.assertEqual(Type.FIVES,  Roll(4, 5, 2, 3, 1).best_upper)
        self.assertEqual(Type.FOURS,  Roll(4, 4, 4, 4, 4).best_upper)
        self.assertEqual(Type.THREES, Roll(1, 1, 3, 3, 1).best_upper)
        self.assertEqual(Type.TWOS,   Roll(1, 1, 2, 2, 1).best_upper)
        self.assertEqual(Type.ACES,   Roll(1, 1, 3, 1, 1).best_upper)

    def testFindLowerBest(self):
        '''Finds best scoring opportunity from lower part of scorepad'''
        self.assertEqual(Type.YAHTZEE,         Roll(4, 4, 4, 4, 4).best_lower)
        self.assertEqual(Type.LARGE_STRAIGHT,  Roll(4, 5, 2, 3, 1).best_lower)
        self.assertEqual(Type.SMALL_STRAIGHT,  Roll(4, 1, 2, 3, 1).best_lower)
        self.assertEqual(Type.FULL_HOUSE,      Roll(5, 5, 2, 2, 5).best_lower)
        self.assertEqual(Type.FOUR_OF_A_KIND,  Roll(1, 1, 5, 1, 1).best_lower)
        self.assertEqual(Type.THREE_OF_A_KIND, Roll(1, 1, 1, 2, 3).best_lower)
        # Chance is a fallback scoring opportunity for the lower half
        self.assertEqual(Type.CHANCE,          Roll(1, 2, 1, 2, 3).best_lower)

    def testConstructorCount(self):
        '''Constructor should take exactly 5 dice rolls'''
        with self.assertRaises(TypeError):
            Roll(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            Roll(1, 2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            Roll([1, 2, 3, 4])
        with self.assertRaises(TypeError):
            Roll([1, 2, 3, 4, 5, 6])

    def testConstructorIterable(self):
        '''Constructor should also allow an iterable as the first argument'''
        self.assertEqual(15, Roll([1, 2, 3, 4, 5]).chance)
        self.assertEqual(15, Roll((1, 2, 3, 4, 5)).chance)
        self.assertEqual(15, Roll(range(1,6)).chance)

    def testEqualRoll(self):
        '''Rolls compare for equality without concern for order'''
        self.assertEqual(Roll(1, 5, 3, 4, 2), Roll(1, 2, 4, 3, 5))
        self.assertEqual(Roll(2, 5, 3, 3, 2), Roll(3, 3, 2, 2, 5))
        self.assertEqual(Roll((2, 5, 3, 3, 2)), Roll([3, 3, 2, 2, 5]))


if __name__ == '__main__':
    system('mypy --disallow-untyped-defs yahtzee.py')
    unittest.main()
