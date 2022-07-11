"""Make a docstring for a public module."""

from random import randint, choice

from brain_games.base_functions import ROUNDS_COUNT

AVAILABLE_OPERATORS = '-+*'
MIN_OPERAND = 1
MAX_OPERAND = 20
CALC_GAME_QUESTION = 'What is the result of the expression?'


def calculate():
    operand1 = randint(MIN_OPERAND, MAX_OPERAND)
    operand2 = randint(MIN_OPERAND, MAX_OPERAND)
    operator = choice(AVAILABLE_OPERATORS)
    if operator == '-':
        question = str(operand1) + ' - ' + str(operand2)
        right_answer = str(operand1 - operand2)
    elif operator == '+':
        question = str(operand1) + ' + ' + str(operand2)
        right_answer = str(operand1 + operand2)
    elif operator == '*':
        question = str(operand1) + ' * ' + str(operand2)
        right_answer = str(operand1 * operand2)
    calculator_output = question, right_answer
    return calculator_output


calc_game_rounds = [calculate() for _ in range(ROUNDS_COUNT)]
