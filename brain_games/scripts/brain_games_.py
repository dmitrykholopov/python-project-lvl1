"""Make a docstring for a public module."""

# !/usr/bin/env python3


from brain_games.base_functions import welcome_user


def main():
    """Add function welcomes user."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
