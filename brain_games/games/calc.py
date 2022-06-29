"""Make a docstring for a public module."""

from random import randint, choice

calc_game_question = 'What is the result of the expression?'


def calculator():
    operand1 = randint(1, 20)
    operand2 = randint(1, 20)
    operator = choice('-+*-+*-+*-+*-+*-+*')
    if operator == '-':
        question = str(operand1) + '-' + str(operand2)
        right_answer = str(operand1 - operand2)
    elif operator == '+':
        question = str(operand1) + '+' + str(operand2)
        right_answer = str(operand1 + operand2)
    elif operator == '*':
        question = str(operand1) + '*' + str(operand2)
        right_answer = str(operand1 * operand2)
    calculator_output = (question, right_answer)
    return calculator_output
