"""Make a docstring for a public module."""

# !/usr/bin/env python3

from brain_games.games.calc import calculate, calc_game_question
from brain_games.games.base_functions import run_game_engine

def main():
    run_game_engine(calculate(),
                    calculate(),
                    calculate(),
                    calc_game_question
                    )


if __name__ == '__main__':
    main()
