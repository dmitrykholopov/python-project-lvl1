"""Make a docstring for a public module."""

from random import randint

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 50
GAME_QUESTION = 'Answer "yes" if the number is prime,' \
                ' otherwise answer "no".'


def is_prime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, 1 + number // 2):
        if number % i == 0:
            return False
    else:
        return True


def get_round_data():
    random_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    question = str(random_number)
    right_answer = 'yes' if is_prime(random_number) else 'no'
    return question, right_answer
