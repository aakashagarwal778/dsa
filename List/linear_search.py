"""
Q. Linear Search Algorithm to locate a card in a list of cards sorted in descending order.
"""

from test_cases import test, tests  # Import shared test cases

def locate_card(cards, query):
    """
    Performs a linear search to locate the position of `query` in the `cards` list.

    Args:
        cards (list of int): A list of integers representing cards, sorted in descending order.
        query (int): The number to search for in the list.

    Returns:
        int: The index of the query in the cards list if found; -1 if not found.
    """
    position = 0  # start at the first index

    # Iterate through the list until the query is found
    while position < len(cards):
        if cards[position] == query:
            return position  # return index immediately if found
        position += 1  # move to the next position

    return -1  # query not found


# Import jovian test evaluation utilities
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

if __name__ == "__main__":
    # Evaluate a single test case
    evaluate_test_case(locate_card, test)
    # Evaluate multiple test cases
    evaluate_test_cases(locate_card, tests)
