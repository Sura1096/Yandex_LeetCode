import pytest
from missing_number import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([3, 0, 1], 2),
                          ([0, 1], 2),
                          ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
                          ([5, 2, 1, 3, 0], 4)])
def test_positive_cases(nums, expected_result):
    assert sol.missingNumber(nums) == expected_result
