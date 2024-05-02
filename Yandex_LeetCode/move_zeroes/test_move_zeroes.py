import pytest
from move_zeroes import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
                          ([0, 0, 0, 1, 0, 3, 12, 0], [1, 3, 12, 0, 0, 0, 0, 0]),
                          ([1, 2, 4, 0, 3, 0, 12, 0], [1, 2, 4, 3, 12, 0, 0, 0])])
def test_positive_cases(nums, expected_result):
    assert sol.moveZeroes(nums) == expected_result
