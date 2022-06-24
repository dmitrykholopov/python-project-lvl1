"""Make a docstring for a public module."""

#!/usr/bin/env python3


from random import randint
from brain_games.games.base_functions import welcome_user, compare_answer


def nod():
    """Add main function with game logic."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):

        right_answer = 1
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        print('Question:', number1, number2)
        if number1 == number2:
            right_answer = number1
        elif number1 > number2:
            number1, number2 = number2, number1
        if number1 < number2:
            for i in range(number1, 1, -1):
                if number2 % i ==0 and number1 % i == 0:
                    right_answer = i
                    break
        right_answer = str(right_answer)

        print('Your answer: ', end='')
        answer = input()
        if compare_answer(right_answer, answer, name):
            continue
        else:
            return
    print('Congratulations, ', name, '!', sep='')
