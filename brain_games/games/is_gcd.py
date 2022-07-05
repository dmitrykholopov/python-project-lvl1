"""Make a docstring for a public module."""

from random import randint

minimum_random_number = 1
maximum_random_number = 50
gcd_game_question = 'Find the greatest common divisor of given numbers.'


def is_gcd():
    """Add main function with game logic."""
    first_number = randint(minimum_random_number, maximum_random_number)
    second_number = randint(minimum_random_number, maximum_random_number)
    right_answer = 1
    if first_number == second_number:
        right_answer = first_number
    elif first_number > second_number:
        first_number, second_number = second_number, first_number
    if first_number < second_number:
        for i in range(first_number, 1, -1):
            if second_number % i == 0 and first_number % i == 0:
                right_answer = i
                break
    question = str(first_number) + ' ' + str(second_number)
    right_answer = str(right_answer)
    gcd_output = question, right_answer
    return gcd_output
