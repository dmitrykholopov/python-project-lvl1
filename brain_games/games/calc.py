"""Make a docstring for a public module."""

#!/usr/bin/env python3


from random import randint, choice
from brain_games.games.base_functions import welcome_user, compare_answer


def is_right_calculated():
    """Add main function with game logic."""
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        operand1 = randint(1, 20)
        operand2 = randint(1, 20)
        operator = choice('-+*-+*-+*-+*-+*-+*')
        print('Question:', end='')
        if operator == '-':
            print(operand1, '-', operand2)
            right_answer = str(operand1 - operand2)
        elif operator == '+':
            print(operand1, '+', operand2)
            right_answer = str(operand1 + operand2)
        elif operator == '*':
            print(operand1, '*', operand2)
            right_answer = str(operand1 * operand2)
        print('Your answer: ', end='')
        answer = input()
        if compare_answer(right_answer, answer, name):
            continue
        else:
            return
    print('Congratulations, ', name, '!', sep='')
