"""Make a docstring for a public module."""

from prompt import string as string

number_of_rounds = 3

def welcome_user():
    """Add function, that ask name & welcomes user."""
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def compare_answer(right_answer, answer, name):
    if right_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}', is wrong answer ;(. "
              f"Correct answer was '{right_answer}'."
              )
        print(f"Let's try again, {name}!")
        return False


def prime_number(number):
    if number == 1:
        return 'no'
    for i in range(1, 1 + number // 2):
        if number % i == 0 and i != 1:
            return 'no'
    return 'yes'


def gcd(number1, number2):
    right_answer = 1
    if number1 == number2:
        right_answer = number1
    elif number1 > number2:
        number1, number2 = number2, number1
    if number1 < number2:
        for i in range(number1, 1, -1):
            if number2 % i == 0 and number1 % i == 0:
                right_answer = i
                break
    return str(right_answer)


def is_right_answer(game_input):
    question, right_answer = game_input
    print(f'Question: {question}')
    print('Your answer: ', end='')
    answer = input()
    if right_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}', is wrong answer ;(. "
              f"Correct answer was '{right_answer}'."
              )
        return False


def run_game_engine(first_round,
                    second_round,
                    third_round, 
                    game_question_const
                    ):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game_question_const)
    rounds = first_round + second_round + third_round
    for i in range(0, number_of_rounds*2, 2):
        if is_right_answer(rounds[i:i + 2]):
            continue
        else:
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
