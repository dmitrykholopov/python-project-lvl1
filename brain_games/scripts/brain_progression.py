# !/usr/bin/env python3

from brain_games.games.progression import identify_missing_number
from brain_games.base_functions import run_game_engine


def main():
    run_game_engine(identify_missing_number)


if __name__ == '__main__':
    main()
