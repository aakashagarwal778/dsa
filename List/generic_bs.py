"""
Generic binary search template using a condition function.
"""

from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
from test_cases import test, tests  # Shared test cases


def binary_search(lo, hi, condition):
    """
    Generic binary search function.

    Args:
        lo (int): Lower bound index.
        hi (int): Upper bound index.
        condition (function): A function that takes `mid` as input and returns:
            - 'found' if the target is found,
            - 'left' if the search should move left,
            - 'right' if the search should move right.

    Returns:
        int: Index of the target if found; -1 otherwise.
    """
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:  # result == 'right'
            lo = mid + 1
    return -1


def locate_card(cards, query):
    """
    Uses the generic binary_search template to locate `query` in a descending sorted list.

    Handles duplicates by returning the first occurrence.
    """

    def condition(mid):
        if cards[mid] == query:
            # Check if this is the first occurrence
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:  # move left in descending list
            return 'left'
        else:
            return 'right'  # move right

    return binary_search(0, len(cards) - 1, condition)


# Run evaluations only if executed directly
if __name__ == "__main__":
    evaluate_test_case(locate_card, test)
    evaluate_test_cases(locate_card, tests)
