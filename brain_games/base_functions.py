"""Make a docstring for a public module."""

from prompt import string as string

ROUNDS_COUNT = 3


def welcome_user():
    """Add function, that ask name & welcomes user."""
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_right_answer(game_input):
    question, right_answer = game_input
    print(f'Question: {question}')
    print('Your answer: ', end='')
    answer = input()
    if right_answer == answer:
        print('Correct!')
        return True
    else:
        print(f'{answer}, is wrong answer ;(. '
              f'Correct answer was {right_answer}.'
              )
        return False


def run_game_engine(game_rounds, game_question_const):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game_question_const)
    for round in game_rounds:
        if is_right_answer(round):
            continue
        else:
            return print(f'Let\'s try again, {name}!')
    print(f'Congratulations, {name}!')
