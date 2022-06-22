"""Make a docstring for a public module."""

#!/usr/bin/env python3

from brain_games.games.calc import is_right_calculated


def main():
    """Add function presents the game."""
    print('Welcome to the Brain Games!')
    is_right_calculated()


if __name__ == '__main__':
    main()
