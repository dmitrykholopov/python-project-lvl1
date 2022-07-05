"""Make a docstring for a public module."""

from random import randint, choice

available_operators = '-+*'
min_operand = 1
max_operand = 20
calc_game_question = 'What is the result of the expression?'


def calculate():
    operand1 = randint(min_operand, max_operand)
    operand2 = randint(min_operand, max_operand)
    operator = choice(available_operators)
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
