"""Make a docstring for a public module."""

from random import randint

maximum_generated_elements = 16     # in fact it's minus 2
minimum_elements_cut = 5
maximum_elements_cut = 10
minimum_step = -5
maximum_step = 5
progression_game_question = (
    'Find the greatest common divisor of given numbers.'
)


def identify_missing_number():
    progression_step = 0
    amount_initial_elements_cutted = randint(
        minimum_elements_cut, maximum_elements_cut
    )
    while progression_step == 0:
        progression_step = randint(minimum_step, maximum_step)
    generated_progression = [
        i * progression_step for i in range(1, maximum_generated_elements)
    ]
    generated_progression = (
        generated_progression[amount_initial_elements_cutted:]
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
