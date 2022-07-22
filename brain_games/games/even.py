"""Make a docstring for a public module."""

from random import randint

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 20
GAME_QUESTION = 'Answer "yes" if the number is even,' \
                ' otherwise answer "no".'


def make_round_data():
    """Add main function with game logic."""
    random_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    question = str(random_number)
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
