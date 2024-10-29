import random
from termcolor import colored

INTERVIEW_MANTRAS = [
    "Form over function - they want to see HOW you think!",
    "Don't forget to breathe - your brain needs oxygen!",
    "Think out loud - your interviewer isn't a mind reader!",
    "Write docstrings first - show them you care about maintainability!",
    "Type hints are your friends - show off that PEP 484 knowledge!",
    "Clean code > clever code - they'll maintain this after you're promoted",
    "Beautiful code tells a story - make it a bestseller",
    "Comment the 'why', not the 'what' - code should be self-documenting",
    "Consistent formatting is key - PEP 8 is your style guide to success",
    "Break it into small, well-named functions - like chapters in your code story",
    "Write tests even if not asked - show them you're production-ready",
    "Git commit messages are documentation - make them proud",
    "Handle errors gracefully - show them you think about edge cases",
    "Use meaningful variable names - future you will thank present you",
    "Structure your code like a good essay - intro, body, conclusion"
]

def random_mantra():
    """
    Get a random interview mantra to calm your nerves.

    Returns:
        str: A colorful, randomly selected mantra about code quality

    Example:
        >>> random_mantra()
        'Clean code > clever code - they'll maintain this after you're promoted'
    """
    return colored(random.choice(INTERVIEW_MANTRAS), 'green')

def all_mantras():
    """
    Print all mantras in a nicely formatted list.

    Each mantra is numbered and color-coded for easy reading.

    Example:
        >>> all_mantras()
        1. Form over function - they want to see HOW you think!
        2. Don't forget to breathe - your brain needs oxygen!
        ...
    """
    for i, mantra in enumerate(INTERVIEW_MANTRAS, 1):
        print(colored(f"{i}. {mantra}", 'green'))