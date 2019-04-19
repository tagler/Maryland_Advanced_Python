'''
Advanced Python Class Assignment - 4/19/2019
'''
from typing import Tuple, Any, Union, Callable
from collections import Counter

# roll object class
class Roll():

    def __init__(self, *args: Any)-> None:

        # multiple tuple value
        if len(args) == 5:
            self.dice = (args)
        # single tuple value (list)
        elif len(args) == 1:
            if len(args[0]) == 5:
                self.dice = (args[0])
            # invalid input
            else:
                raise TypeError
        # invalid input
        else:
            raise TypeError

        # confirms input are ints
        for each in self.dice:
            if isinstance(each, int) == False:
                raise TypeError

        # counts number of dice at each value
        cnt: Counter = Counter()
        for each_dice in self.dice:
            cnt[each_dice] += 1
        self.cnt = cnt

    # equal operator
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Roll):
            return NotImplemented
        for each_pair in zip(sorted(self.dice), sorted(other.dice)):
            if each_pair[0] != each_pair[1]:
                return False
        return True

    # upper score properties
    @property
    def aces(self) -> int:
        return self.cnt[1]
    @property
    def twos(self) -> int:
        return self.cnt[2]*2
    @property
    def threes(self)-> int:
        return self.cnt[3]*3
    @property
    def fours(self)-> int:
        return self.cnt[4]*4
    @property
    def fives(self)-> int:
        return self.cnt[5]*5
    @property
    def sixes(self)-> int:
        return self.cnt[6]*6

    # lower score properties
    @property
    def three_of_a_kind(self) -> int:
        if (3 in list(self.cnt.values()) or
            4 in list(self.cnt.values()) or
            5 in list(self.cnt.values())):
            return sum(self.dice)
        return 0
    @property
    def four_of_a_kind(self) -> int:
        if (4 in list(self.cnt.values()) or
            5 in list(self.cnt.values())):
            return sum(self.dice)
        return 0
    @property
    def full_house(self) -> int:
        if (2 in list(self.cnt.values()) and
            3 in list(self.cnt.values())):
            return 25
        return 0
    @property
    def small_straight(self) -> int:
        if (1 in self.dice and
            2 in self.dice and
            3 in self.dice and
            4 in self.dice):
            return 30
        if (2 in self.dice and
            3 in self.dice and
            4 in self.dice and
            5 in self.dice):
            return 30
        if (3 in self.dice and
            4 in self.dice and
            5 in self.dice and
            6 in self.dice):
            return 30
        return 0
    @property
    def large_straight(self) -> int:
        if (1 in self.dice and
            2 in self.dice and
            3 in self.dice and
            4 in self.dice and
            5 in self.dice):
            return 40
        if (2 in self.dice and
            3 in self.dice and
            4 in self.dice and
            5 in self.dice and
            6 in self.dice):
            return 40
        return 0
    @property
    def yahtzee(self) -> int:
        if 5 in list(self.cnt.values()):
            return 50
        return 0
    @property
    def chance(self) -> int:
        return sum(self.dice)

    # returns integer value of specified type
    def score_as(self, score_type: 'Type') -> int:
        if score_type == Type.ACES:
            return self.aces
        elif score_type == Type.TWOS:
            return self.twos
        elif score_type == Type.THREES:
            return self.threes
        elif score_type == Type.FOURS:
            return self.fours
        elif score_type == Type.FIVES:
            return self.fives
        elif score_type == Type.SIXES:
            return self.sixes
        elif score_type == Type.THREE_OF_A_KIND:
            return self.three_of_a_kind
        elif score_type == Type.FOUR_OF_A_KIND:
            return self.four_of_a_kind
        elif score_type == Type.FULL_HOUSE:
            return self.full_house
        elif score_type == Type.SMALL_STRAIGHT:
            return self.small_straight
        elif score_type == Type.LARGE_STRAIGHT:
            return self.large_straight
        elif score_type == Type.YAHTZEE:
            return self.yahtzee
        elif score_type == Type.CHANCE:
            return self.chance
        return 0

    # returns best score from upper section
    @property
    def best_upper(self) -> 'Callable[[Type], Type]':
        upper_scores = [self.aces,
                        self.twos,
                        self.threes,
                        self.fours,
                        self.fives,
                        self.sixes]
        upper_types = [Type.ACES,
                       Type.TWOS,
                       Type.THREES,
                       Type.FOURS,
                       Type.FIVES,
                       Type.SIXES]
        # finds max score via perfered order
        upper_score_max = max(upper_scores)
        for index, each_score in enumerate(upper_scores):
            if each_score == upper_score_max:
                upper_score_max_arg = index
                break
        return upper_types[upper_score_max_arg]

    # returns best score from lower section
    @property
    def best_lower(self) -> 'Callable[[Type], Type]':
        lower_scores = [self.yahtzee,
                        self.large_straight,
                        self.small_straight,
                        self.full_house,
                        self.four_of_a_kind,
                        self.three_of_a_kind,
                        self.chance]
        lower_types = [Type.YAHTZEE,
                       Type.LARGE_STRAIGHT,
                       Type.SMALL_STRAIGHT,
                       Type.FULL_HOUSE,
                       Type.FOUR_OF_A_KIND,
                       Type.THREE_OF_A_KIND,
                       Type.CHANCE]
        # finds max score via perfered order
        lower_score_max = max(lower_scores)
        for index, each_score in enumerate(lower_scores):
            if each_score == lower_score_max:
                lower_score_max_arg = index
                break
        return lower_types[lower_score_max_arg]


# type object class
class Type():
    # properties for all score types
    @property
    def ACES(self) -> 'Type':
        return self.ACES
    @property
    def TWOS(self) -> 'Type':
        return self.TWOS
    @property
    def THREES(self) -> 'Type':
        return self.THREES
    @property
    def FOURS(self) -> 'Type':
        return self.FOURS
    @property
    def FIVES(self) -> 'Type':
        return self.FIVES
    @property
    def SIXES(self) -> 'Type':
        return self.SIXES
    @property
    def CHANCE(self) -> 'Type':
        return self.CHANCE
    @property
    def THREE_OF_A_KIND(self) -> 'Type':
        return self.THREE_OF_A_KIND
    @property
    def FOUR_OF_A_KIND(self) -> 'Type':
        return self.FOUR_OF_A_KIND
    @property
    def FULL_HOUSE(self) -> 'Type':
        return self.FULL_HOUSE
    @property
    def SMALL_STRAIGHT(self) -> 'Type':
        return self.SMALL_STRAIGHT
    @property
    def LARGE_STRAIGHT(self) -> 'Type':
        return self.LARGE_STRAIGHT
    @property
    def YAHTZEE(self) -> 'Type':
        return self.YAHTZEE
