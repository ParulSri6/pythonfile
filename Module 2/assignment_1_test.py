import pytest
from io import StringIO
from contextlib import redirect_stdout

# Import the functions from the solution files
from assignment_1 import get_two_numbers_and_calculate, calculate_seconds_from_days


def test_get_two_numbers_100_50_and_calculate(monkeypatch):
    inputs = iter(['100', '50'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        get_two_numbers_and_calculate()

    output = f.getvalue()
    assert "Sum is 150" in output
    assert "Multiplication is 5000" in output
    assert "Division is 2" in output


def test_get_two_numbers_45_9_and_calculate(monkeypatch):
    inputs = iter(['45', '9'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        get_two_numbers_and_calculate()

    output = f.getvalue()
    assert "Sum is 54" in output
    assert "Multiplication is 405" in output
    assert "Division is 5" in output


def test_calculate_seconds_from_7_days(monkeypatch):
    inputs = iter(['7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        calculate_seconds_from_days()

    output = f.getvalue()
    assert "7 days have 604800 seconds" in output

def test_calculate_seconds_from_90_days(monkeypatch):
    inputs = iter(['90'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        calculate_seconds_from_days()

    output = f.getvalue()
    assert "90 days have 7776000 seconds" in output