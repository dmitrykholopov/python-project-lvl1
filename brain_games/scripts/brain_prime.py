
"""Make a docstring for a public module."""

# !/usr/bin/env python3

from brain_games.games.is_prime import prime_game_question
from brain_games.games.is_prime import is_prime
from brain_games.games.base_functions import run_game_engine


def main():
    run_game_engine(is_prime(),
                    is_prime(),
                    is_prime(),
                    prime_game_question
                    )


if __name__ == '__main__':
    main()
