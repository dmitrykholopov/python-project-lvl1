"""Make a docstring for a public module."""

from random import randint
from brain_games.games.base_functions import welcome_user, compare_answer,\
    gcd


def nod():
    """Add main function with game logic."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        print(f'Question: {number1} {number2}')
        print('Your answer: ', end='')
        answer = input()
        if compare_answer(gcd(number1, number2), answer, name):
            continue
        else:
            return
    print(f'Congratulations, {name}!')
