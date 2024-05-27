import pytest
from subarray_sums_divisible_by_k import Solution


sol = Solution()


@pytest.mark.parametrize('nums, k, expected_result',
                         [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 6),
                          ([5], 9, 0),
                          ([1, 2, 3, 4, 5], 3, 7),
                          ([2, 2, 2, 2, 2], 2, 15),
                          ([5, 10, 15, 20, 25], 5, 15)])
def test_positive_numbers(nums, k, expected_result):
    assert sol.subarraysDivByK(nums, k) == expected_result
