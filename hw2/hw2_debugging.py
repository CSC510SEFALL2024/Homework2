"""
This module implements the merge sort algorithm with a helper function
to recombine sorted sub-arrays.

"""

import rand


def merge_sort(input_arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        input_arr (list): The array to be sorted.

    Returns:
        list: Sorted array.
    """
    if len(input_arr) <= 1:  # Removed unnecessary parentheses
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(
        input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Combines two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left half of the array.
        right_arr (list): The right half of the array.

    Returns:
        list: A sorted array combining left_arr and right_arr.
    """
    left_index = 0
    right_index = 0
    merged_arr = []  # Use an empty list to avoid fixed-size initialization

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merged_arr.append(right_arr[right_index])
            right_index += 1

    # Extend remaining elements of both arrays
    merged_arr.extend(right_arr[right_index:])
    merged_arr.extend(left_arr[left_index:])

    return merged_arr


# Generate a random array of size 20 and sort it
arr = rand.random_array([None] * 20)
sorted_arr = merge_sort(arr)

print(sorted_arr)
