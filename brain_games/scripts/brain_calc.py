"""Make a docstring for a public module."""

# !/usr/bin/env python3


from brain_games.games.calc import calculator, calc_game_question
from brain_games.games.base_functions import welcome_user, is_right_answer


def main():
    """Add function presents the game."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(calc_game_question)
    for _ in range(3):
        if is_right_answer(calculator()):
            continue
        else:
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
