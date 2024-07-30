import pytest
from io import StringIO
from contextlib import redirect_stdout

# Import the function from the solution file
from quadratic_equation_assignment_2 import solve_quadratic_equation


def test_solve_quadratic_equation_case_1(monkeypatch):
    inputs = iter(['1', '2', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        solve_quadratic_equation()

    output = f.getvalue()
    assert "Result:" in output
    assert "x1 = x2 = -1.0" in output


def test_solve_quadratic_equation_case_2(monkeypatch):
    inputs = iter(['1', '-7', '12'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        solve_quadratic_equation()

    output = f.getvalue()
    assert "Result:" in output
    assert "x1 = 4.0" in output
    assert "x2 = 3.0" in output


def test_solve_quadratic_equation_case_3(monkeypatch):
    inputs = iter(['1', '1', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        solve_quadratic_equation()

    output = f.getvalue()
    assert "Result:" in output
    assert "There are no real solutions" in output


def test_solve_quadratic_equation_case_4(monkeypatch):
    inputs = iter(['0', '1', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        solve_quadratic_equation()

    output = f.getvalue()
    assert "Result:" in output
    assert "This is not a valid quadratic equation" in output
