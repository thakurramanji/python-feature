import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()


    def test_multiplicatio(self):
        self.assertEqual(self.calc.multiply(-1,0), 0);
        self.assertEqual(self.calc.multiply(-1,-1), 1);


        # self.assertEqual(self.calc.add(1, 2), 3)
        # self.assertEqual(self.calc.add(-1, 1), 0)
        # self.assertEqual(self.calc.add(-1, -1), -2)

    # def test_subtract(self):
    #     self.assertEqual(self.calc.subtract(10, 5), 5)
    #     self.assertEqual(self.calc.subtract(-1, 1), -2)
    #     self.assertEqual(self.calc.subtract(-1, -1), 0)
    #
    # def test_multiply(self):
    #     self.assertEqual(self.calc.multiply(3, 7), 21)
    #     self.assertEqual(self.calc.multiply(-1, 1), -1)
    #     self.assertEqual(self.calc.multiply(-1, -1), 1)
    #
    # def test_divide(self):
    #     self.assertEqual(self.calc.divide(10, 2), 5)
    #     self.assertEqual(self.calc.divide(-1, 1), -1)
    #     self.assertEqual(self.calc.divide(-1, -1), 1)
    #
    #     with self.assertRaises(ValueError):
    #         self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
