import unittest
from RIPASSO.ripasso import Calc

class TestCalculations(unittest.TestCase):

    def setUp(self) -> None:
        self.calculation = Calc(8,2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(),10,'The sum is wrong.')

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(),7,'The sum is wrong.')

    


if __name__ == "__main__":
    unittest.main()
