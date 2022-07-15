# !/usr/bin/env python3

from brain_games.games.even import is_even
from brain_games.base_functions import run_game_engine


def main():
    """Add function presents the game."""
    run_game_engine(is_even)


if __name__ == '__main__':
    main()
