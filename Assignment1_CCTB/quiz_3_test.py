import pytest
from io import StringIO
from contextlib import redirect_stdout

# Import the function from the solution file
from quiz_3 import terraform_mars


def test_terraform_mars_case_1(monkeypatch):
    inputs = iter([
        '-60', '500', '500',
        'greenhouse', 'co2', 'melting',
        '20', '1200', '6000'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature too low" in output
    assert "Using greenhouse gases" in output
    assert "Pressure too low" in output
    assert "Releasing CO2" in output
    assert "Water too low" in output
    assert "Melting ice caps" in output
    assert "Mars habitable!" in output


def test_terraform_mars_case_2(monkeypatch):
    inputs = iter([
        '10', '900', '1200',
        '15', '1000', '4000'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature tolerable" in output
    assert "Pressure sufficient" in output
    assert "Water sufficient" in output
    assert "Continue terraforming" in output


def test_terraform_mars_case_3(monkeypatch):
    inputs = iter([
        '0', '1000', '2000',
        '5', '1200', '5500'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature tolerable" in output
    assert "Pressure sufficient" in output
    assert "Water sufficient" in output
    assert "Mars habitable!" in output


def test_terraform_mars_case_4(monkeypatch):
    inputs = iter([
        '-70', '300', '800',
        'space mirrors', 'co2', 'importing',
        '-60', '1000', '1500'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature too low" in output
    assert "Using space mirrors" in output
    assert "Pressure too low" in output
    assert "Releasing CO2" in output
    assert "Water too low" in output
    assert "Importing water" in output
    assert "Continue terraforming" in output


def test_terraform_mars_case_5(monkeypatch):
    inputs = iter([
        '-80', '800', '500',
        'nuclear', 'importing',
        '10', '900', '6000'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature too low" in output
    assert "Using nuclear reactors" in output
    assert "Pressure sufficient" in output
    assert "Water too low" in output
    assert "Importing water" in output
    assert "Continue terraforming" in output


def test_terraform_mars_case_6(monkeypatch):
    inputs = iter([
        '-55', '550', '300',
        'space mirrors', 'co2', 'extracting',
        '5', '700', '4000'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature too low" in output
    assert "Using space mirrors" in output
    assert "Pressure too low" in output
    assert "Releasing CO2" in output
    assert "Water too low" in output
    assert "Extracting from soil" in output
    assert "Continue terraforming" in output


def test_terraform_mars_case_7(monkeypatch):
    inputs = iter([
        '-15', '1500', '700',
        'melting',
        '5', '900', '5000'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature tolerable" in output
    assert "Pressure sufficient" in output
    assert "Water too low" in output
    assert "Melting ice caps" in output
    assert "Continue terraforming" in output


def test_terraform_mars_case_8(monkeypatch):
    inputs = iter([
        '-80', '600', '900',
        'greenhouse', 'invalid',
        '-10', '800', '1100'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature too low" in output
    assert "Using greenhouse gases" in output
    assert "Pressure sufficient" in output
    assert "Water too low" in output
    assert "Defaulting to melting ice caps" in output
    assert "Continue terraforming" in output


def test_terraform_mars_case_9(monkeypatch):
    inputs = iter([
        '-70', '100', '120',
        'invalid', 'invalid', 'invalid',
        '10', '1100', '2000'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature too low" in output
    assert "Defaulting to using greenhouse gases" in output
    assert "Pressure too low" in output
    assert "Defaulting to releasing CO2" in output
    assert "Water too low" in output
    assert "Defaulting to melting ice caps" in output
    assert "Continue terraforming" in output


def test_terraform_mars_case_10(monkeypatch):
    inputs = iter([
        '-100', '200', '800',
        'nuclear', 'volcanic', 'extracting',
        '-5', '1000', '500'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    f = StringIO()
    with redirect_stdout(f):
        terraform_mars()

    output = f.getvalue()
    assert "Temperature too low" in output
    assert "Using nuclear reactors" in output
    assert "Pressure too low" in output
    assert "Simulating volcanoes" in output
    assert "Water too low" in output
    assert "Extracting from soil" in output
    assert "Continue terraforming" in output
