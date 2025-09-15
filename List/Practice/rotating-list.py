"""
Assignment 1 - Rotated Sorted List Search
-----------------------------------------
We'll solve the problem step by step:
1. Brute Force Linear Scan to find rotation count
2. Modified Binary Search to find rotation count efficiently
"""

# ----------------------------------------
# 1. BRUTE FORCE APPROACH (Linear Scan)
# ----------------------------------------
def count_rotations_linear(nums):
    """
    Count the number of rotations in a rotated sorted array using linear scan.
    Returns the index of the smallest element.
    Time Complexity: O(n)
    """
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position += 1
    return 0  # array not rotated


# ---------------------------------------------------
# 2. MODIFIED BINARY SEARCH (Rotated Sorted Array)
# ---------------------------------------------------
def count_rotations_binary(nums):
    lo = 0  # start of array
    hi = len(nums) - 1  # end of array

    while lo <= hi:  # loop until search space is exhausted
        mid = (lo + hi) // 2
        mid_number = nums[mid]

        # Uncomment the next line for logging values
        # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        # Check if mid is the rotation point
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid  # mid is the index of smallest element

        # If left half is sorted, rotation point must be in right half
        elif nums[mid] >= nums[lo]:
            lo = mid + 1

            # Otherwise, rotation point is in left half
        else:
            hi = mid - 1

    return 0  # array is not rotated

# ----------------------------------------
# 3. Run Tests Using Jovian's Evaluate Module
# ----------------------------------------
from test_cases import tests  # Shared test cases
from jovian.pythondsa import evaluate_test_cases

if __name__ == "__main__":
    print("\nLinear Scan Rotation Count Results:")
    evaluate_test_cases(count_rotations_linear, tests)

    print("\nBinary Search Rotation Count Results:")
    evaluate_test_cases(count_rotations_binary, tests)


