import random
from termcolor import colored

PANIC_RESPONSES = [
    "Take a deep breath. The interviewer is probably just as nervous about making a good impression.",
    "Remember: You've prepared for this. And if not, well, there's always another interview!",
    "Worst case scenario? You get some great practice and a funny story.",
    "Plot twist: Maybe YOU'RE interviewing THEM!",
    "Fun fact: The more interviews you bomb, the better your success stories become.",
    "Remember: They're not testing your knowledge, they're testing your Google-fu without Google.",
    "Pro tip: 'I don't know, but here's how I'd figure it out' is a perfectly valid answer.",
]

def emergency_therapy():
    """Get an emergency pep talk when you're panicking."""
    return colored(random.choice(PANIC_RESPONSES), 'magenta')

def stress_level(level=5):
    """Rate your stress level (1-10) and get appropriate advice."""
    if level <= 3:
        return colored("You're doing great! Maybe too great... are you a robot?", 'blue')
    elif level <= 7:
        return colored("Perfect stress level! Just enough to keep you sharp.", 'green')
    else:
        return colored("CODE RED! Time for some deep breaths and emergency_therapy()!", 'red')