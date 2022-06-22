"""Add a docstring for a public module."""

from prompt import string
import scripts.games.base_functions

def welcome_user():
    """Add function, that ask name & welcomes user."""
    name = string('May I have your name? ')
    print('Hello ', name, '!')
    return name
