"""
The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function. A
typical example of a test function that implements checking that a certain input leads to an expected output.
"""

import pytest


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5])
def test_numbers(number):
    """
    mark can be used to apply "inline" parameterization, without a fixture
    """
    print("\nRunning test_numbers with {}".format(number))


@pytest.mark.parametrize("inputs, expected", [
    ((1, 2), 3),
    ((3, 5), 8),
    (("Sica", "ra"), "Sicara")
])
def test_expected_sum(inputs, expected):
    """
    mark.parametrize can even unpack tuples into named parameters
    """
    print("\nRunning test_expected with {} as input and {} as expected output".format(inputs, expected))
    assert inputs[0] + inputs[1] == expected
