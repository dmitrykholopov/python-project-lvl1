"""Make a docstring for a public module."""

from random import randint, choice

AVAILABLE_OPERATORS = ['-', '+', '*']
MIN_OPERAND = 1
MAX_OPERAND = 20
GAME_QUESTION = 'What is the result of the expression?'


def play_the_game():
    operand1 = randint(MIN_OPERAND, MAX_OPERAND)
    operand2 = randint(MIN_OPERAND, MAX_OPERAND)
    operator = choice(AVAILABLE_OPERATORS)
    if operator == '-':
        question = f'{operand1} - {operand2}'
        right_answer = str(operand1 - operand2)
    elif operator == '+':
        question = f'{operand1} + {operand2}'
        right_answer = str(operand1 + operand2)
    elif operator == '*':
        question = f'{operand1} * {operand2}'
        right_answer = str(operand1 * operand2)
    return question, right_answer
