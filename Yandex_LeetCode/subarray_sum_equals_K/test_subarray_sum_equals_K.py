import pytest
from subarray_sum_equals_K import Solution


sol = Solution()


@pytest.mark.parametrize('nums, k, expected_result',
                         [([1, 1, 1], 2, 2),
                          ([1, 2, 3], 3, 2),
                          ([1, 2, 3, 7, 19, 2, 45, 6, 8, 34], 10, 1)])
def test_positive_nums(nums, k, expected_result):
    assert sol.subarraySum(nums, k) == expected_result


@pytest.mark.parametrize('nums, k, expected_result',
                         [([-1, 8, -5, 9, 4, 3, -3, 4, 6, 12, 10, 1, 5, -19, -22], 0, 1),
                          ([-1, 1, -1, 1, 0, 0, 2, -2], 0, 16),
                          ([-1, -1, -2, -2, -2, 4, 2, 2, 3], 6, 2)])
def test_negative_nums(nums, k, expected_result):
    assert sol.subarraySum(nums, k) == expected_result


