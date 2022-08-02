"""Module generating data for the progression game"""

from random import randint

PROGRESSION = {
    'min_length': 10,
    'max_length': 15,
    'min_first_element': 30,
    'max_first_element': 50,
    'min_step': 1,
    'max_step': 10
}
GAME_QUESTION = 'What number is missing in the progression?'


def get_progression(progression):
    progression_step = randint(
        progression['min_step'],
        progression['max_step']
    )
    progression_first_elem = randint(
        progression['min_first_element'],
        progression['max_first_element']
    )
    progression_elements_count = randint(
        progression['min_length'],
        progression['max_length']
    )
    return [i for i in range(
            progression_first_elem,
            progression_first_elem
            + progression_elements_count
            * progression_step,
            progression_step
            )]


def get_round_data():
    generated_progression = get_progression(PROGRESSION)
    hidden_element = randint(0, len(generated_progression) - 1)
    right_answer = str(generated_progression.pop(hidden_element))
    generated_progression.insert(hidden_element, '..')
    question = ''
    for element in generated_progression:
        question += str(element) + ' '
    question = question.rstrip()
    return question, right_answer
