import pytest

from p1330 import compare


@pytest.mark.parametrize(
    ("num1", "num2", "result"),
    [
        (1, 2, "<"),
        (19, 2, ">"),
        (5, 5, "=="),
    ],
)
def test_compare(num1, num2, result):
    assert compare(num1, num2) == result
