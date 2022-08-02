#!/usr/bin/env python3

from brain_games.games import even
from brain_games.game_engine import run_game_engine


def main():
    """Add function presents the game."""
    run_game_engine(even)


if __name__ == '__main__':
    main()
