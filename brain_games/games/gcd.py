"""Module generating data for the gcd game"""

from random import randint
from math import gcd

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 50
GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def get_round_data():
    """Add main function with game logic."""
    first_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    second_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    question = f'{first_number} {second_number}'
    right_answer = str(gcd(first_number, second_number))
    return question, right_answer
