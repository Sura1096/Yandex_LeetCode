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


@pytest.mark.parametrize('nums, k, expected_result',
                         [([5], 9, 0),
                          ([2, 2, 2, 2, 2], 2, 15),
                          ([-10, 10, -10, 10], 5, 10),
                          ([0, 0, 0, 0], 5, 10),
                          ([1, 2, 3], 1000, 0)])
def test_boundary_cases(nums, k, expected_result):
    assert sol.subarraysDivByK(nums, k) == expected_result


@pytest.mark.parametrize('expected_exception, nums, k',
                         [(ValueError, [], 2),
                          (ValueError, [1, 2] * (3 * 10**4 + 1), 2),
                          (TypeError, [1, 2, 3], 'a'),
                          (ValueError, [1, 2, 3], 0),
                          (ValueError, [1, 2, 3], 10 * 10**4),
                          (TypeError, [2, 2, 2, ';', 4, 1, 3], 4),
                          (ValueError, [7, -1, -3, 6 * -10**4, 9, 5], 110),
                          (ValueError, [-1, -1, -2, -4, 10 * 10**4, 11, 12], 1000)])
def test_error_cases(expected_exception, nums, k):
    with pytest.raises(expected_exception):
        sol.subarraysDivByK(nums, k)
