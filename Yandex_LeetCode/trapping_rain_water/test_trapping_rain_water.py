import unittest
from trapping_rain_water import Solution


class TestTrappingWater(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_function_output(self):
        self.assertEqual(
            self.sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]),
            6
        )

        self.assertEqual(
            self.sol.trap([4, 2, 0, 3, 2, 5]),
            9
        )

        self.assertEqual(
            self.sol.trap([1]),
            0
        )

        self.assertEqual(
            self.sol.trap([2, 0, 2]),
            2
        )


if __name__ == '__main__':
    unittest.main()