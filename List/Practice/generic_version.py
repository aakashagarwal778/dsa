# ----------------------------------------
#. Generic Binary Search Template
# ----------------------------------------

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


def count_rotations_generic(nums):
    def condition(mid):
        mid_number = nums[mid]

        # Check if mid is the rotation point
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return "found"

        # If left half is sorted, rotation point is in right half
        if nums[0] <= nums[mid]:
            return "right"

        # Otherwise, rotation point is in left half
        return "left"

    return binary_search(0, len(nums) - 1, condition)


# Run Tests cases
from test_cases import tests  # Shared test cases
from jovian.pythondsa import evaluate_test_cases

if __name__ == "__main__":
    print("\nGeneric Binary Search Rotation Count Results:")
    evaluate_test_cases(count_rotations_generic, tests)
