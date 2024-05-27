import pytest


def cal(a: int, b: int) -> int:

    return (a + b) * (a - b)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 3, 7),
        (3, 4, -7),
    ],
)
def cal_2(a, b, expected):
    assert cal(a, b) == expected


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(cal(a, b))
