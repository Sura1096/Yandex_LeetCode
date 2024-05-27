import pytest
from subarray_sums_divisible_by_k import Solution


sol = Solution()


@pytest.mark.parametrize('nums, k, expected_result',
                         [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 6),
                          ([1, 2, 3, 4, 5], 3, 7),
                          ([5, 10, 15, 20, 25], 5, 15)])
def test_positive_numbers(nums, k, expected_result):
    assert sol.subarraysDivByK(nums, k) == expected_result


@pytest.mark.parametrize('nums, k, expected_result',
                         [([4, 5, 0, -2, -3, 1], 5, 7),
                          ([-1, 2, 9, -3, 7, 1], 5, 4),
                          ([3, -1, -2, 5, 6], 4, 2)])
def test_negative_numbers(nums, k, expected_result):
    assert sol.subarraysDivByK(nums, k) == expected_result
