"""Make a docstring for a public module."""

# !/usr/bin/env python3

from brain_games.games.is_gcd import GCD_GAME_QUESTION
from brain_games.games.is_gcd import is_gcd_game_rounds
from brain_games.base_functions import run_game_engine


def main():
    run_game_engine(is_gcd_game_rounds, GCD_GAME_QUESTION)


if __name__ == '__main__':
    main()
