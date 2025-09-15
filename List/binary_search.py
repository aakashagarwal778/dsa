# binary_search.py
"""
Binary search implementation for locating a card in a descending sorted list of cards by turning over a fewest cards possible.
With the least complexity O(log n).
"""

from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
from test_cases import test, tests  # Import shared test cases

def test_location(cards, query, mid):
    """
    Helper function to decide which side to continue searching.
    Returns 'found', 'left', or 'right'.
    """
    mid_number = cards[mid]
    #print("mid:", mid, ", mid_number:", mid_number)

    if mid_number == query:
        # Check if this is the first occurrence
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'  # search left side in descending array
    else:
        return 'right'  # search right side

def locate_card(cards, query):
    """
    Binary search function to locate the query in descending sorted cards.
    Returns index of the query if found, -1 otherwise.
    """
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        #print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

if __name__ == "__main__":
    # Evaluate using Jovian test utilities
    evaluate_test_case(locate_card, test)
    evaluate_test_cases(locate_card, tests)
