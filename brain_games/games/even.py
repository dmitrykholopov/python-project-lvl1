"""Make a docstring for a public module."""

#!/usr/bin/env python3


from random import randint
from brain_games.games.base_functions import welcome_user, compare_answer


def is_even():
    """Add main function with game logic."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = randint(1, 20)
        print('Question: ', random_number)
        print('Your answer: ', end='')
        answer = input()
        if random_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if compare_answer(right_answer, answer, name):
            continue
        else:
            return
    print('Congratulations, ', name, '!', sep='')
