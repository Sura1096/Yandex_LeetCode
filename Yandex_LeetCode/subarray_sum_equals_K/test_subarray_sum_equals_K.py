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


@pytest.mark.parametrize('nums, k, expected_result',
                         [([-1], 0, 0),
                          ([0], 0, 1),
                          ([1, 2, 3, 4, 5, 6], 17, 0)])
def test_boundary_cases(nums, k, expected_result):
    assert sol.subarraySum(nums, k) == expected_result


@pytest.mark.parametrize('expected_exception, nums, k',
                         [(ValueError, [], 2),
                          (ValueError, [1] * (3 * 10**4), 3),
                          (TypeError, [1, 2, 3, 4], 'a'),
                          (ValueError, [1, 2, 3, 4], 3 * (-10**7)),
                          (ValueError, [1, 2], 2 * 10**7),
                          (TypeError, [1, 2, 3, 'a', 4, 5], 5),
                          (ValueError, [1, 2, 3, 4 * (-1000), 5], 67),
                          (ValueError, [1, 2, 4, 9 * 1000], 4)])
def test_errors(expected_exception, nums, k):
    with pytest.raises(expected_exception):
        sol.subarraySum(nums, k)
