"""
Holds tests
"""
from src import simple


def test_answer():
    assert simple.increment(3) == 4


def test_add():
    assert simple.add(1, 3) == 4


def test_subtract():
    assert simple.subtract(15, 2) == 13


def test_multiply():
    assert simple.multiply(10, 10) == 100
