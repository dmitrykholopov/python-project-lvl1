"""Make a docstring for a public module."""

from random import randint

minimum_random_number = 1
maximum_random_number = 20
even_game_question = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)


def is_even():
    """Add main function with game logic."""
    random_number = randint(minimum_random_number, maximum_random_number)
    question = str(random_number)
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    even_output = question, right_answer
    return even_output
