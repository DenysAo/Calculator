from unittest import TestCase, main
from calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-4'), -1)

    def test_multi(self):
        self.assertEqual(calculator('4*4'), 16)

    def test_divide(self):
        self.assertEqual(calculator('10/5'), 2.0)

    def test_no_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('The expression must contain at least one operator (+-/*)', e.exception.args[0])

    def test_two_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('The expression must contain 2 integers and 1 operator', e.exception.args[0])

    def test_many_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('The expression should contain 2 integers and 1 operator', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2 + 3.0')
        self.assertEqual('The expression must contain 2 integers and 1 operator', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('The expression should contain 2 integers and 1 operator', e.exception.args[0])


if __name__ == '__main__':
    main()