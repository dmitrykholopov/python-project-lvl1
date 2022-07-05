"""Make a docstring for a public module."""

# !/usr/bin/env python3

from brain_games.games.progression import progression_game_question
from brain_games.games.progression import identify_missing_number
from brain_games.games.base_functions import run_game_engine


def main():
    run_game_engine(identify_missing_number(),
                    identify_missing_number(),
                    identify_missing_number(),
                    progression_game_question
                    )


if __name__ == '__main__':
    main()
