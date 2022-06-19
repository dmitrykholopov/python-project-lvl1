"""Make a docstring for a public module."""

# !/usr/bin/env python


#   from prompt import string
from random import randint, choice
from prompt import string


def welcome_user():
    """Add function, that ask name & welcomes user."""
    global name
    name = string('May I have your name? ')
    return print('Hello, ', name, '!')


def compare_answer_calc(right_answer, answer):
    if right_answer ==  answer:
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


def is_right_calculated():
    """Add main function with game logic."""
    welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        random_number = randint(1, 20)
        random_number2 = randint(1, 20)
        operator = choice('-+*-+*-+*-+*-+*-+*')
        print('Question: ', end='')
        if operator == '-':
            print(random_number, '-', random_number2)
            right_answer = str(random_number - random_number2)
        elif operator == '+':
            print(random_number, '+', random_number2)
            right_answer = str(random_number + random_number2)
        elif operator == '*':
            print(random_number, '*', random_number2)
            right_answer = str(random_number * random_number2)
        print('Your answer: ', end='')
        answer = input()
        if compare_answer_calc(right_answer, answer):
            continue
        else:
            return False
    print('Congratulations, ', name, '!', sep='')


def main():
    """Add function presents the game."""
    print('Welcome to the Brain Games!')
    is_right_calculated()


if __name__ == '__main__':
    main()
