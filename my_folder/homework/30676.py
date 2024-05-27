import pytest


def color(frequency: int) -> str:
    if 620 <= frequency <= 780:
        return "Red"
    if 590 <= frequency <= 620:
        return "Orange"
    if 570 <= frequency <= 590:
        return "Yellow"
    if 495 <= frequency <= 570:
        return "Green"
    if 450 <= frequency <= 495:
        return "Blue"
    if 425 <= frequency <= 450:
        return "Indigo"
    if 380 <= frequency <= 425:
        return "Violet"


@pytest.mark.parametrize(
    "frequency, expected",
    [
        (627, "Red"),
        (516, "Green"),
    ],
)
def color_2(frequency: int, expected: str):
    assert color(frequency) == expected


if __name__ == "__main__":
    frequency = int(input())
    print(color(frequency))
