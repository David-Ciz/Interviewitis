# showcase_interviewitis.py

"""
🎭 Interview Preparation Showcase
===============================

A demonstration of the interviewitis package capabilities to help you nail
that technical interview! This showcase includes examples of all major features
with real-world scenarios.

Author: Your Name
License: MIT
Version: 1.0.0

Usage:
    $ python showcase_interviewitis.py

Pro tip: Read through the code before your interview - it's full of good practices!
"""

import time
from typing import Dict, List, Optional
from termcolor import colored
from interviewitis import (
    random_mantra,
    refresh_definition,
    emergency_therapy,
    stress_level,
    list_terms
)


def showcase_mantras(count: int = 3) -> None:
    """
    Showcase the interview mantras feature with a nice countdown effect.

    Args:
        count: Number of mantras to display
    """
    print(colored("\n=== 📢 Daily Interview Mantras ===", 'cyan', attrs=['bold']))
    print(colored("Remember these pearls of wisdom:", 'cyan'))

    for i in range(count):
        time.sleep(1)  # Build a little suspense
        print(f"\n{i + 1}. {random_mantra()}")


def practice_definitions(terms: Optional[List[str]] = None) -> Dict[str, str]:
    """
    Practice key technical definitions you might need in the interview.

    Args:
        terms: List of terms to review. If None, uses a default set.

    Returns:
        Dict mapping terms to their definitions

    Example:
        >>> results = practice_definitions(['pep8', 'docker_container'])
        >>> print(results['pep8'])
        'Python Enhancement Proposal 8: Style guide for Python...'
    """
    if terms is None:
        terms = ['pep8', 'microservices', 'docker_image', 'fastapi', 'solid']

    print(colored("\n=== 📚 Technical Definition Review ===", 'yellow', attrs=['bold']))

    results = {}
    for term in terms:
        print(f"\n🔍 Reviewing: {term}")
        definition = refresh_definition(term)
        results[term] = definition
        print(definition)
        time.sleep(0.5)  # Give time to read each definition

    return results


def handle_interview_stress(stress_levels: List[int]) -> None:
    """
    Demonstrate the stress management features with different scenarios.

    Args:
        stress_levels: List of stress levels to simulate (1-10)
    """
    print(colored("\n=== 🧘‍♂️ Stress Management Corner ===", 'magenta', attrs=['bold']))

    for level in stress_levels:
        print(f"\nScenario: Your stress level is {level}/10")
        print(stress_level(level))

        if level > 7:
            print("\n🚨 Emergency therapy activated!")
            print(emergency_therapy())

        time.sleep(1)


def available_resources() -> None:
    """Display all available terms in the package for quick reference."""
    print(colored("\n=== 📋 Available Reference Terms ===", 'green', attrs=['bold']))
    terms = list_terms()

    # Create a nice columnar output
    column_width = max(len(term) for term in terms) + 2
    columns = 3

    for i in range(0, len(terms), columns):
        row_terms = terms[i:i + columns]
        row = "".join(term.ljust(column_width) for term in row_terms)
        print(colored(row, 'green'))


if __name__ == "__main__":
    """
    Main showcase function demonstrating the complete package capabilities.
    """
    print(colored("""
        🎯 Interviewitis Package Showcase
        ================================
        Your technical interview survival kit!
        """, 'white', attrs=['bold']))

    # Show some mantras to get in the right mindset
    showcase_mantras()

    # Practice key definitions
    practice_definitions()

    # Demonstrate stress management
    handle_interview_stress([3, 6, 9])

    # Show available resources
    available_resources()

    print(colored("""
        ✨ End of Showcase ✨
        Remember: You've got this! The interviewer is just another developer who
        was once in your shoes.
        """, 'white', attrs=['bold']))