# test_number_analysis.py

import pytest
from io import StringIO
from contextlib import redirect_stdout
from quiz_5 import list_squares


def test_positive_numbers(monkeypatch):
    inputs = iter(['5', '3', '2', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        list_squares(input_function=input)

    output = f.getvalue()
    assert "5 25" in output
    assert "3 9" in output
    assert "2 4" in output


def test_negative_number(monkeypatch):
    inputs = iter(['5', '-1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        list_squares(input_function=input)

    output = f.getvalue()
    assert "5 25" in output
    assert "Negative number entered, stopping program." in output


def test_invalid_input_then_zero(monkeypatch):
    inputs = iter(['5', 'a', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        list_squares(input_function=input)

    output = f.getvalue()
    assert "5 25" in output
    assert "Invalid input, please enter a positive integer." in output
    assert "Error message: invalid literal for int() with base 10: 'a'" in output
    assert "Zero entered, stopping input." in output


def test_all_invalid_inputs_then_zero(monkeypatch):
    inputs = iter(['a', 'b', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        list_squares(input_function=input)

    output = f.getvalue()
    assert "Invalid input, please enter a positive integer." in output
    assert "Error message: invalid literal for int() with base 10: 'a'" in output
    assert "Error message: invalid literal for int() with base 10: 'b'" in output
    assert "Zero entered, stopping input." in output


def test_large_numbers(monkeypatch):
    inputs = iter(['1000', '2000', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        list_squares(input_function=input)

    output = f.getvalue()
    assert "1000 1000000" in output
    assert "2000 4000000" in output


def test_float_input(monkeypatch):
    inputs = iter(['5', '4.5', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        list_squares(input_function=input)

    output = f.getvalue()
    assert "5 25" in output
    assert "Invalid input, please enter a positive integer." in output
    assert "Error message: invalid literal for int() with base 10: '4.5'" in output


def test_special_character_input(monkeypatch):
    inputs = iter(['5', '#', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        list_squares(input_function=input)

    output = f.getvalue()
    assert "5 25" in output
    assert "Invalid input, please enter a positive integer." in output
    assert "Error message: invalid literal for int() with base 10: '#'" in output
