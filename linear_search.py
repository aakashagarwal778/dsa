# Define a single test case
test = {
    'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7},
    'output': 3
}

# Define multiple test cases to validate the function
tests = [
    test,  # query occurs in the middle
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},  # query near the end
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},  # query is first element
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},  # query is last element
    {'input': {'cards': [6], 'query': 6}, 'output': 0},  # single-element list
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},  # query not present
    {'input': {'cards': [], 'query': 7}, 'output': -1},  # empty list
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},  # repeated numbers
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}  # multiple occurrences
]


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

# Evaluate a single test case
evaluate_test_case(locate_card, test)

# Evaluate multiple test cases
evaluate_test_cases(locate_card, tests)
