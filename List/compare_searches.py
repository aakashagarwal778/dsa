# compare_searches.py
"""
Compare performance of linear search vs binary search on a large input.
"""

from jovian.pythondsa import evaluate_test_case
from linear_search import locate_card as locate_card_linear
from binary_search import locate_card as locate_card_binary

# Large test case: 10 million descending cards, query near the end
large_test = {
    'input': {
        'cards': list(range(10_000_000, 0, -1)),
        'query': 2
    },
    'output': 9_999_998  # Index of the query
}

# Linear search evaluation
result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)
print("Linear Search:")
print("Result: {}\nPassed: {}\nExecution Time: {:.3f} ms".format(result, passed, runtime))

# Binary search evaluation
result, passed, runtime = evaluate_test_case(locate_card_binary, large_test, display=False)
print("\nBinary Search:")
print("Result: {}\nPassed: {}\nExecution Time: {:.3f} ms".format(result, passed, runtime))
