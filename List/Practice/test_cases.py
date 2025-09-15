# ----------------------------------------
# TEST CASES (Complete Set)
# ----------------------------------------
tests = [
    {"input": {"nums": [6,7,8,9,1,2,3,4,5]}, "output": 4},  # rotation in middle
    {"input": {"nums": [1,2,3,4,5,6,7,8,9]}, "output": 0},  # no rotation
    {"input": {"nums": [3,4,5,1,2]}, "output": 3},
    {"input": {"nums": [2,3,4,5,1]}, "output": 4},
    {"input": {"nums": [1]}, "output": 0},                  # single element
    {"input": {"nums": []}, "output": 0},                   # empty array
    {"input": {"nums": [5,1,2,3,4]}, "output": 1},          # rotation at index 1
    {"input": {"nums": [4,5,1,2,3]}, "output": 2},          # rotation at index 2       # rotation at index 2
    ]