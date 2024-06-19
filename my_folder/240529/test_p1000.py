import pytest

from p1000 import add


def test_add():
    assert add(1, 2) == 3


def test_add():
    assert add(2, 3) == 5


def test_add():
    assert add(4, 5) == 9
