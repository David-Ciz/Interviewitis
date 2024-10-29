from termcolor import colored

COMMON_DEFINITIONS = {
    "big_o": "Big O notation describes the upper bound (worst case) of time/space complexity",
    "solid": "SOLID: Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion",
    "rest": "REST: Representational State Transfer - stateless, cacheable, client-server architecture",
    "acid": "ACID: Atomicity, Consistency, Isolation, Durability - database transaction properties",
    "cap_theorem": "CAP: Consistency, Availability, Partition tolerance - pick two!",
    "pep8": "Python Enhancement Proposal 8: Style guide for Python code. 4 spaces indent, max 79 chars per line, snake_case for functions, PascalCase for classes",
    "pep484": "PEP 484: Type hints in Python. Lets you annotate variables, function params, and return types (e.g., def greet(name: str) -> str)",
    "pep20": "PEP 20: The Zen of Python. 'Beautiful is better than ugly', 'Explicit is better than implicit', 'Simple is better than complex'",
    "microservices": "Architecture where app is collection of loosely coupled, independently deployable services. Each service does ONE thing well (unlike your ex)",
    "monolith": "Traditional architecture where all functionality is in one codebase. Easier to develop, harder to scale (like your Netflix queue)",
    "django": "Full-featured Python web framework with 'batteries included'. ORM, admin interface, authentication - the Swiss Army knife of frameworks",
    "fastapi": "Modern, fast Python web framework based on type hints. Async by default, automatic API docs, minimal but mighty",
    "flask": "Lightweight, extensible Python web framework. 'Microframework' that scales up, not down. Like a LEGO set - build what you need",
    "docker_image": "Read-only template with instructions for creating a container. Like a recipe for your application (ingredients + cooking instructions)",
    "docker_container": "Running instance of a Docker image. Like the actual meal you cooked from the recipe. Can have many containers from one image",
    "mvc": "MVC: Model (data), View (UI), Controller (logic) - but everyone implements it differently",
    "api_gateway": "Single entry point for all client API calls to microservices. Like a smart receptionist who knows where everyone sits",
    "orm": "Object-Relational Mapping: Converts between incompatible type systems (Python objects <-> database tables). Like a translator for your data",
}


def refresh_definition(term):
    """
    Get a refresher on a common CS term.

    Args:
        term (str): The technical term to look up

    Returns:
        str: Colored definition of the term, or a friendly message if not found

    Examples:
        >>> refresh_definition('pep8')
        # Returns colorful explanation of PEP 8
        >>> refresh_definition('unknown')
        # Returns friendly "not found" message
    """
    term = term.lower()
    if term in COMMON_DEFINITIONS:
        return colored(f"{term}: {COMMON_DEFINITIONS[term]}", 'yellow')
    return colored("Term not found. But hey, maybe that's an opportunity to learn something new!", 'red')

def list_terms():
    """
    List all available terms that can be looked up.

    Returns:
        list: Sorted list of all available technical terms

    Example:
        >>> list_terms()
        ['acid', 'api_gateway', 'big_o', 'cap_theorem', ...]
    """
    return list(COMMON_DEFINITIONS.keys())