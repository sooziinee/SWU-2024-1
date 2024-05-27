import pytest


def cal(string: str) -> int:
    result = 0
    vowel = {"a", "e", "i", "o", "u"}
    for char in string:
        if char in vowel:
            result += 1
    return result


@pytest.mark.parametrize(
    "string, expected",
    [
        ("joiyosen", 4),
        ("bitaro", 3),
    ],
)
def cal_2(string: str, expected: int):
    assert cal(string) == expected


if __name__ == "__main__":
    _ = input()
    string = input()
    print(cal(string))
