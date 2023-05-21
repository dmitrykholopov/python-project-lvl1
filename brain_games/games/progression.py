"""Module generating data for the progression game"""

from random import randint

#   progression data:
MIN_MAX_LENGTH = 10, 15
MIN_MAX_FIRST_ELEMENT = 30, 50
MIN_MAX_STEP = 1, 10

GAME_QUESTION = 'What number is missing in the progression?'


def get_progression(min_max_length,
                    min_max_first_element,
                    min_max_step
                   ):
    progression_step = randint(min_max_step)
    progression_first_elem = randint(min_max_first_element)
    progression_elements_count = randint(min_max_length)

    return [i for i in range(
            progression_first_elem,
            progression_first_elem
            + progression_elements_count
            * progression_step,
            progression_step
            )]


def get_round_data():
    generated_progression = get_progression(MIN_MAX_LENGTH,
                                            MIN_MAX_FIRST_ELEMENT,
                                            MIN_MAX_STEP)
    
    hidden_element = randint(0, len(generated_progression) - 1)
    right_answer = str(generated_progression.pop(hidden_element))
    generated_progression.insert(hidden_element, '..')
    question = ''

    for element in generated_progression:
        question += str(element) + ' '
    question = question.rstrip()

    return question, right_answer
