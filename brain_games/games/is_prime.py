"""Make a docstring for a public module."""

from random import randint

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 50
GAME_QUESTION = 'Answer "yes" if the number is prime,' \
                ' otherwise answer "no".'


def get_round_data():
    random_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    question = str(random_number)
    right_answer = 'yes'
    if random_number == 1 or random_number == 0:
        right_answer = 'no'
    for i in range(2, 1 + random_number // 2):
        if random_number % i == 0:
            right_answer = 'no'
    return question, right_answer
