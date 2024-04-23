import pytest
from max_consecutive_ones import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([1, 1, 0, 1, 1, 1], 3),
                          ([1, 0, 1, 1, 0, 1], 2),
                          ([1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], 5)])
def test_positive_cases(nums, expected_result):
    assert sol.findMaxConsecutiveOnes(nums) == expected_result
