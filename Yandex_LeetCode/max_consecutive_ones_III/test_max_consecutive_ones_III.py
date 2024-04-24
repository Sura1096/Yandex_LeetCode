import pytest
from max_consecutive_ones_III import Solution


sol = Solution()


@pytest.mark.parametrize('nums, k, expected_result',
                         [([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
                          ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
                          ([1, 1, 1, 0, 0, 1, 1, 0], 4, 8)])
def test_positive_cases(nums, k, expected_result):
    assert sol.longestOnes(nums, k) == expected_result
