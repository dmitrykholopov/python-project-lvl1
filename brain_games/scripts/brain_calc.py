# !/usr/bin/env python3

from brain_games.games.calc import calculate
from brain_games.base_functions import run_game_engine


def main():
    run_game_engine(calculate)


if __name__ == '__main__':
    main()
