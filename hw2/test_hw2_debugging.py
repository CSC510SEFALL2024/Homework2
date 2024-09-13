"""
This module contains unit tests for the merge_sort function.
"""

# Importing the required modules
from hw2_debugging import merge_sort

def test_merge_sort_1():
    """
    Test merge_sort with an already sorted array of integers.
    """
    input_arr = [1, 8, 16, 32, 64]
    output_expected = [1, 8, 16, 32, 64]
    assert merge_sort(input_arr) == output_expected

def test_merge_sort_2():
    """
    Test merge_sort with a reverse sorted array of integers.
    """
    input_arr = [15, 14, 13, 12, 11]
    output_expected = [11, 12, 13, 14, 15]
    assert merge_sort(input_arr) == output_expected

def test_merge_sort_3():
    """
    Test merge_sort with an unsorted array of integers, including negative numbers.
    """
    input_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, -1, -3, 0, -100]
    output_expected = [-100, -3, -1, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert merge_sort(input_arr) == output_expected
