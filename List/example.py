"""
Q. Find the first and last positions of a target in an ascending sorted array
using a reusable binary search template.
"""

from generic_bs import binary_search  # Reuse our generic binary_search


def first_position(nums, target):
    """
    Finds the first occurrence of `target` in a sorted array `nums`.

    Args:
        nums (list of int): Ascending sorted list of numbers.
        target (int): The number to locate.

    Returns:
        int: Index of the first occurrence of target, or -1 if not found.
    """

    def condition(mid):
        if nums[mid] == target:
            # Move left if a duplicate exists
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):
    """
    Finds the last occurrence of `target` in a sorted array `nums`.

    Args:
        nums (list of int): Ascending sorted list of numbers.
        target (int): The number to locate.

    Returns:
        int: Index of the last occurrence of target, or -1 if not found.
    """

    def condition(mid):
        if nums[mid] == target:
            # Move right if a duplicate exists
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    """
    Returns the first and last positions of `target` in `nums`.

    Args:
        nums (list of int): Ascending sorted list of numbers.
        target (int): Number to locate.

    Returns:
        tuple: (first_index, last_index)
    """
    return first_position(nums, target), last_position(nums, target)


# Optional: test example if run directly
if __name__ == "__main__":
    nums = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    print("Array:", nums)
    print("Target:", target)
    print("First and Last Positions:", first_and_last_position(nums, target))
    # Output should be (1, 3)
