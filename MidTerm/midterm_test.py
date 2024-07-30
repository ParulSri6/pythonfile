import pytest

from midterm import (
    sum_of_even_numbers,
    count_vowels,
    reverse_string,
    replace_consonants,
    find_maximum,
    merge_dicts,
    fibonacci,
    pig_latin,
    number_replacer,
    fizzpop,
    caesar_encode,
    caesar_decode,
)


def test_sum_of_even_numbers():
    assert sum_of_even_numbers([1, 2, 3, 4, 5]) == 6
    assert sum_of_even_numbers([10, 15, 20, 25, 30]) == 60
    assert sum_of_even_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30


def test_count_vowels():
    assert count_vowels("hello world") == 3
    assert count_vowels("AEIOUaeiou") == 10
    assert count_vowels("python programming is fun!") == 6


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("racecar") == "racecar"


def test_replace_consonants():
    assert replace_consonants("hello") == "*e**o"
    assert replace_consonants("world") == "*o***"
    assert replace_consonants("PYTHON") == "****O*"


def test_find_maximum():
    assert find_maximum([1, 2, 3, 4, 5]) == 5
    assert find_maximum([-10, 0, 10, 20, 30]) == 30
    assert find_maximum([-5, -1, -10, -3]) == -1


def test_merge_dicts():
    assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {'a': 1, 'b': 3, 'c': 4}
    assert merge_dicts({"x": 5}, {"y": 10, "x": 7}) == {'x': 7, 'y': 10}
    assert merge_dicts({"a": 1, "b": 2, "c": 3}, {"d": 4}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_pig_latin():
    assert pig_latin("hello world") == "ellohay orldway"
    assert pig_latin("python programming") == "ythonpay rogrammingpay"
    assert pig_latin("algorithm") == "algorithmway"


def test_number_replacer():
    assert number_replacer([1, 2, 3, 2, 4], 2, 5) == [1, 5, 3, 5, 4]
    assert number_replacer([10, 20, 30, 20, 40], 20, 50) == [10, 50, 30, 50, 40]
    assert number_replacer([5, 6, 7, 5, 8], 5, 10) == [10, 6, 7, 10, 8]


def test_fizzpop():
    assert fizzpop(5) == ['1', '2', 'Fizz', '4', 'Pop']
    assert fizzpop(15) == ['1', '2', 'Fizz', '4', 'Pop', 'Fizz', '7', '8', 'Fizz', 'Pop', '11', 'Fizz', '13', '14',
                           'FizzPop']
    assert fizzpop(20) == ['1', '2', 'Fizz', '4', 'Pop', 'Fizz', '7', '8', 'Fizz', 'Pop', '11', 'Fizz', '13', '14',
                           'FizzPop', '16', '17', 'Fizz', '19', 'Pop']


# More complex tests for Caesar Cipher functions
def test_caesar_encode():
    assert caesar_encode("hello", 3) == "khoor"
    assert caesar_encode("Python", 5) == "Udymts"
    assert caesar_encode("xyz", 29) == "abc"
    assert caesar_encode("alphabet", -9) == "rcgyrsvk"
    assert caesar_encode("volanic", 12) == "haxmzuo"
    assert caesar_encode("supercalifragilisticexpialidocious", 14) == "gidsfqozwtfouwzwghwqsldwozwrcqwcig"


def test_caesar_decode():
    assert caesar_decode("khoor", 3) == "hello"
    assert caesar_decode("Udymts", 5) == "Python"
    assert caesar_decode("abc", -23) == "xyz"
