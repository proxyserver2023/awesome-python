import pytest
from capital_case import *


def test_capital_case():
    assert capital_case('alamin') == 'Alamin'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
