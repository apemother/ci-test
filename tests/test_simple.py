"""
Holds tests
"""


def inc(x):
    return x + 1


def subtract(x, y):
    return x - y


def add(x, y):
    return x + y


def test_answer():
    assert inc(3) == 4


def test_add():
    assert add(1, 3) == 4


def test_true_equal_false():
    assert True == False


def test_subtract():
    assert subtract(15, 2) == 13
