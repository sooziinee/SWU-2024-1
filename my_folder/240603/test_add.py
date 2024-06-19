import pytest

from add import add


@pytest.mark.parametrize(
    ("a", "b", "expeected"),
    [
        (1, 2, 3),
        (3, 4, 7),
        (5, 6, 11),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
