
"""Make a docstring for public package."""

# file __init__.py

__name__ = 'functions'

from prompt import string
from brain_games.games.base_functions import welcome_user, compare_answer

__all__ = [
    'welcome_user',
    'compare_answer',
    'string'
]
