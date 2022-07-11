"""Make a docstring for a public module."""

from random import randint

from brain_games.base_functions import ROUNDS_COUNT

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 20
EVEN_GAME_QUESTION = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)


def is_even():
    """Add main function with game logic."""
    random_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    question = str(random_number)
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    even_output = question, right_answer
    return even_output


even_game_rounds = [is_even() for _ in range(ROUNDS_COUNT)]
