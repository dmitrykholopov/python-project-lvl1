"""Make a docstring for a public module."""

from random import randint

minimum_random_number = 1
maximum_random_number = 50
prime_game_question = (
    'Answer "yes" if the number is prime, otherwise answer "no".'
)


def is_prime():
    random_number = randint(minimum_random_number, maximum_random_number)
    question = str(random_number)
    right_answer = 'yes'
    if random_number == 1:
        right_answer = 'no'
    for i in range(1, 1 + random_number // 2):
        if random_number % i == 0 and i != 1:
            right_answer = 'no'
    prime_output = question, right_answer
    return prime_output
