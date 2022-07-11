"""Make a docstring for a public module."""

# !/usr/bin/env python3

from brain_games.games.calc import CALC_GAME_QUESTION
from brain_games.games.calc import calc_game_rounds
from brain_games.base_functions import run_game_engine


def main():
    run_game_engine(calc_game_rounds, CALC_GAME_QUESTION)


if __name__ == '__main__':
    main()
