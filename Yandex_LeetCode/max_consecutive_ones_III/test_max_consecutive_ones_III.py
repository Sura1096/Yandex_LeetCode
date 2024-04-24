import pytest
from max_consecutive_ones_III import Solution


sol = Solution()


@pytest.mark.parametrize('nums, k, expected_result',
                         [([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
                          ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
                          ([1, 1, 1, 0, 0, 1, 1, 0], 3, 8),
                          ([1, 1, 1, 0, 0, 1, 1, 0], 4, 8)])
def test_positive_cases(nums, k, expected_result):
    assert sol.longestOnes(nums, k) == expected_result


@pytest.mark.parametrize('nums, k, expected_result',
                         [([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 0, 4),
                          ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 0, 4),
                          ([1, 1, 1, 0, 0, 1, 1, 0], 0, 3),
                          ([1, 1, 1, 1, 1, 1, 1, 1], 3, 8),
                          ([1, 1, 1, 1, 1, 1, 1, 1], 3, 8),
                          ([0, 0, 0, 0, 0, 0, 0, 0], 0, 0),
                          ([0, 0, 0, 0, 0, 0, 0, 0], 8, 8)])
def test_boundary_cases(nums, k, expected_result):
    assert sol.longestOnes(nums, k) == expected_result
