
"""Make a docstring for a public module."""

# !/usr/bin/env python


from prompt import string
from random import randint


def welcome_user():
    """Add function, that ask name & welcomes user."""
    global name
    name = string('May I have your name? ')
    return print('Hello, ', name, '!')


# def compare_answer_first(random_number, answer):
#     if (
#             (random_number % 2 == 0 and answer == 'yes')
#             or (random_number % 2 != 0 and answer == 'no')
#         ):
#             print('Correct!')
#             return True
#     elif (
#             (random_number % 2 == 0 and answer != 'yes')
#             or (random_number % 2 != 0 and answer != 'no')
#         ):
#             print(
#                 "'", answer, "'",
#                 ' is wrong answer ;(. Correct answer was ',
#                 "'", random_number, "'.", sep=''
#             )
#             print("Let's try again, ", name, '!', sep='')
#             return False


def compare_answer(random_number, answer):
    if random_number % 2 == 0 and answer == 'yes':
        print('Correct!')
        return True
    elif random_number % 2 != 0 and answer == 'no':
        print('Correct!')
        return True
    else:
        print(
            "'", answer, "'",
            ' is wrong answer ;(. Correct answer was ',
            "'", random_number, "'.", sep=''
        )
        print("Let's try again, ", name, '!', sep='')
        return False


def is_even():
    """Add main function with game logic."""
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = randint(1, 20)
        print('Question: ', random_number)
        print('Your answer: ', end='')
        answer = input()
        if compare_answer(random_number, answer):
            continue
        else:
            return False
    print('Congratulations, ', name, '!', sep='')


def main():
    """Add function presents the game."""
    print('Welcome to the Brain Games!')
    is_even()


if __name__ == '__main__':
    main()
