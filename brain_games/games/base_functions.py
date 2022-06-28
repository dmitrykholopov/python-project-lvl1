"""Make a docstring for a public module."""

from prompt import string as string


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
