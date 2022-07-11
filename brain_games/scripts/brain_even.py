"""Make a docstring for a public module."""

# !/usr/bin/env python3

from brain_games.games.even import EVEN_GAME_QUESTION
from brain_games.games.even import even_game_rounds
from brain_games.base_functions import run_game_engine


def main():
    """Add function presents the game."""
    run_game_engine(even_game_rounds, EVEN_GAME_QUESTION)


if __name__ == '__main__':
    main()
