"""Make a docstring for a public module."""

#!/usr/bin/env python3


from random import randint
from brain_games.games.base_functions import welcome_user, compare_answer


def arithmetic_progressoin():
    """Add main function with game logic."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        d = 0
        cutting_elements = randint(5, 10)
        while d == 0:
            d = randint(-5, 5)
        generated_progression = [i * d for i in range(1, 16)]
        generated_progression = generated_progression[cutting_elements:]
        hidden_element = randint(0, len(generated_progression) - 1)
        right_answer = str(generated_progression.pop(hidden_element))
        generated_progression.insert(hidden_element, '..')
        print('Question:', *generated_progression)
        print('Your answer: ', end='')
        answer = input()
        if compare_answer(right_answer, answer, name):
            continue
        else:
            return
    print('Congratulations, ', name, '!', sep='')
