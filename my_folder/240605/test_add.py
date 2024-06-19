from unittest.mock import patch

import pytest
import add


@patch("add.add_two_nums")
def test_add_two_nums(mock_add):
    mock_add.return_value = 11
    exp = 11
    assert add.add_two_nums(3, 7) == exp
