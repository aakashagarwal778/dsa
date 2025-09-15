# test_cases.py
# Contains all test cases for both linear and binary search

test = {
    'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7},
    'output': 3
}

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
