from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a = 1000
        b = 500
        cal = Calculator()

        result = cal.subtract(a, b)

        expected = 500
        assert result == expected

    def test_multiply(self):
        a = 10
        b = 20
        cal = Calculator()

        result = cal.multiply(a, b)

        expected = 200
        assert result == expected

    def test_divide(self):
        a = 100
        b = 10
        cal = Calculator()

        result = cal.divide(a, b)

        expected = 10
        assert result == expected