"""Make a docstring for a public module."""

# !/usr/bin/env python3

from brain_games.games.is_gcd import gcd_game_question
from brain_games.games.is_gcd import is_gcd
from brain_games.games.base_functions import run_game_engine


def main():
    run_game_engine(is_gcd(),
                    is_gcd(),
                    is_gcd(),
                    gcd_game_question
                    )


if __name__ == '__main__':
    main()
