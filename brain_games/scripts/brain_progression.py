"""Make a docstring for a public module."""

# !/usr/bin/env python3

from brain_games.games.progression import PROGRESSION_GAME_QUESTION
from brain_games.games.progression import prograssion_game_rounds
from brain_games.base_functions import run_game_engine


def main():
    run_game_engine(prograssion_game_rounds, PROGRESSION_GAME_QUESTION)


if __name__ == '__main__':
    main()
