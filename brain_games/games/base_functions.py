"""Make a docstring for a public module."""

#!/usr/bin/env python3

# __all__ = ['welcome_user', 'compare_answer', 'name', 'string']

from prompt import string as string


def welcome_user():
    """Add function, that ask name & welcomes user."""
    name = string('May I have your name? ')
    print('Hello, ', name, '!', sep='')
    return name


def compare_answer(right_answer, answer, name):
    if right_answer == answer:
        print('Correct!')
        return True
    else:
        print(
            "'", answer, "'",
            ' is wrong answer ;(. Correct answer was ',
            "'", right_answer, "'.", sep=''
        )
        print("Let's try again, ", name, '!', sep='')
        return False
