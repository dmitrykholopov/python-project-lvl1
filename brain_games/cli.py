"""Add a docstring for a public module."""

from prompt import string


def welcome_user():
    """Add function, that ask name & welcomes user."""
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
