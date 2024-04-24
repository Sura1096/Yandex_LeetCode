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
                          ([0, 0, 0, 0, 0, 0, 0, 0], 8, 8),
                          ([0], 1, 1),
                          ([1], 0, 1),
                          ([1], 1, 1)])
def test_boundary_cases(nums, k, expected_result):
    assert sol.longestOnes(nums, k) == expected_result


@pytest.mark.parametrize('expected_exception, nums, k',
                         [(ValueError, [], 1),
                          (ValueError, [1, 1, 1, 1], 10),
                          (ValueError, [1] * (10**5 + 1), 2),
                          (ValueError, [0, 1, 0, 1], -1),
                          (ValueError, [1, 1, 1, 0, 0, 1, 3], 2),
                          (ValueError, [1, 2, 3, 4, 5], 3),
                          (ValueError, [1, 1, 1, 'a', 0, 0], 4),
                          (ValueError, ['a', 'b', 'c'], 0)])
def test_errors(expected_exception, nums, k):
    with pytest.raises(expected_exception):
        sol.longestOnes(nums, k)
