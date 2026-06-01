import unittest
from discount_logic import calculate_discount

class TestDiscountCalculator(unittest.TestCase):
    def test_normal_discount(self):
        result = calculate_discount(100, 20)
        self.assertEqual(result, 80.0)

if __name__ == '__main__':
    unittest.main()


