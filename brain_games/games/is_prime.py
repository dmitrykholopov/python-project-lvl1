"""Make a docstring for a public module."""

from random import randint

from brain_games.base_functions import ROUNDS_COUNT

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 50
PRIME_GAME_QUESTION = (
    'Answer "yes" if the number is prime, otherwise answer "no".'
)


def is_prime():
    random_number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    question = str(random_number)
    right_answer = 'yes'
    if random_number == 1 or random_number == 0:
        right_answer = 'no'
    for i in range(1, 1 + random_number // 2):
        if random_number % i == 0 and i != 1:
            right_answer = 'no'
    prime_output = question, right_answer
    return prime_output


is_prime_game_rounds = [is_prime() for _ in range(ROUNDS_COUNT)]
