"""Make a docstring for a public module."""

from prompt import string

ROUNDS_COUNT = 3


def welcome_user():
    """Add function, that ask name & welcomes user."""
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game_engine(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.GAME_QUESTION)
    for _ in range(ROUNDS_COUNT):
        question, right_answer = game.get_round_data()
        print(f'Question: {question}')
        answer = string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
            continue
        else:
            print(f'{answer}, is wrong answer ;(. '
                  f'Correct answer was {right_answer}.'
                  )
            print(f'Let\'s try again, {name}!')      
            return
    print(f'Congratulations, {name}!')

