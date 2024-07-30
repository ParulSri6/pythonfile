import pytest
from quiz_2 import reverse_list, replace_value, count_number_duplicates


def test_reverse_list():
    original_list = [1, 2, 2, 5, 8, 4, 4, 8, 2, 1, 6]
    expected_reversed = [6, 1, 2, 8, 4, 4, 8, 5, 2, 2, 1]
    assert reverse_list(original_list) == expected_reversed


def test_replace_value():
    original_list = [1, 2, 2, 5, 8, 4, 4, 8, 2, 1, 6]
    expected_replaced = [1, 2, 2, 10, 8, 4, 4, 8, 2, 1, 6]
    assert replace_value(original_list, 5, 10) == expected_replaced


def test_count_duplicates():
    original_list = [1, 2, 2, 5, 8, 4, 4, 8, 2, 1, 6]
    expected_duplicates_count = 5  # 1: 1 times, 2: 2 times, 4: 1 times, 8: 1 times
    assert count_number_duplicates(original_list) == expected_duplicates_count
