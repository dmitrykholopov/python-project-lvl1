#!/usr/bin/env python3

from brain_games.games import is_prime
from brain_games.base_functions import run_game_engine


def main():
    run_game_engine(is_prime)


if __name__ == '__main__':
    main()
