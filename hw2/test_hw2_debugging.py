import pytest
from hw2_debugging import merge_sort

def test_merge_sort_1():
    input_arr = [1, 8, 16, 32, 64]
    output_expected = [1, 8, 16, 32, 64]
    assert merge_sort(input_arr) == output_expected

def test_merge_sort_2():
    input_arr = [15, 14, 13, 12, 11]
    output_expected = [11, 12, 13, 14, 15]
    assert merge_sort(input_arr) == output_expected

def test_merge_sort_3():
    input_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, -1, -3, 0, -100]
    outputexpected = [-100, -3, -1, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert merge_sort(input_arr) == outputexpected
