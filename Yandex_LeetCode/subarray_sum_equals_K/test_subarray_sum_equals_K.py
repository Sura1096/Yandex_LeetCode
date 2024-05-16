import pytest
from subarray_sum_equals_K import Solution


sol = Solution()


@pytest.mark.parametrize('nums, k, expected_result',
                         [([1, 1, 1], 2, 2),
                          ([1, 2, 3], 3, 2),
                          ([1, 2, 3, 7, 19, 2, 45, 6, 8, 34], 10, 1)])
def test_positive_nums(nums, k, expected_result):
    assert sol.subarraySum(nums, k) == expected_result


