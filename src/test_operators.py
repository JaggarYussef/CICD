"""
Unit tests for the calculator library
"""

import operators


class TestOperators:

    def test_addition(self):
        assert 4 == operators.add(2, 2)

    def test_subtraction(self):
        assert 2 == operators.subtract(4, 2)