"""Make a docstring for a public module."""

from random import randint

from brain_games.base_functions import ROUNDS_COUNT

MAXIMUM_GENERATED_ELEMENTS_COUNT = 16     # in fact it's minus 2
MINIMUM_ELEMENTS_CUT_COUNT = 5
MAXIMUM_ELEMENTS_CUT_COUNT = 10
MINIMUM_STEP = -5
MAXIMUM_STEP = 5
PROGRESSION_GAME_QUESTION = 'What number is missing in the progression?'


def identify_missing_number():
    progression_step = 0
    initial_elements_cutted_count = randint(
        MINIMUM_ELEMENTS_CUT_COUNT,
        MAXIMUM_ELEMENTS_CUT_COUNT
    )
    while progression_step == 0:
        progression_step = randint(MINIMUM_STEP, MAXIMUM_STEP)
    generated_progression = [
        i * progression_step for i in range(1, MAXIMUM_GENERATED_ELEMENTS_COUNT)
    ]
    generated_progression = (
        generated_progression[initial_elements_cutted_count:]
    )
    hidden_element = randint(0, len(generated_progression) - 1)
    right_answer = str(generated_progression.pop(hidden_element))
    generated_progression.insert(hidden_element, '..')
    question = ''
    for element in generated_progression:
        question += str(element) + ' '
    question = question.rstrip()
    progression_output = question, right_answer
    return progression_output


prograssion_game_rounds = [
    identify_missing_number() for _ in range(ROUNDS_COUNT)
]
