"""Make a docstring for a public module."""

from random import randint
from math import gcd

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 50
GCD_GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def is_gcd():
    """Add main function with game logic."""
    first_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    second_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    question = str(first_number) + ' ' + str(second_number)
    right_answer = str(gcd(first_number, second_number))
    return question, right_answer, GCD_GAME_QUESTION
