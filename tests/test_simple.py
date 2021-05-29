"""
Holds tests
"""
import src.simple as simp


def test_answer():
    assert simp.increment(3) == 4


def test_add():
    assert simp.add(1, 3) == 4


def test_subtract():
    assert simp.subtract(15, 2) == 13


def test_multiply():
    assert simp.multiply(10, 10) == 100
