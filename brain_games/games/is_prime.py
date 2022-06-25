"""Make a docstring for a public module."""

# !/usr/bin/env python3


from random import randint
from brain_games.games.base_functions import welcome_user, compare_answer,\
    is_prime_number


def prime():
    """Add main function with game logic."""
    name = welcome_user()
    print('Answer "yes" if the number is prime, otherwise answer "no".')
    for _ in range(3):
        random_number = randint(1, 50)
        print('Question:', random_number)
        print('Your answer: ', end='')
        answer = input()
        if compare_answer(is_prime_number(random_number), answer, name):
            continue
        else:
            return
    print('Congratulations, ', name, '!', sep='')
