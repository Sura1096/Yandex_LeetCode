import pytest
from max_consecutive_ones import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([1, 1, 0, 1, 1, 1], 3),
                          ([1, 0, 1, 1, 0, 1], 2),
                          ([1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], 5)])
def test_positive_cases(nums, expected_result):
    assert sol.findMaxConsecutiveOnes(nums) == expected_result


@pytest.mark.parametrize('nums, expected_result',
                         [([1, 1, 1, 1, 1, 1], 6),
                          ([0, 0, 0, 0, 0, 0], 0),
                          ([1], 1),
                          ([0], 0)])
def test_boundary_cases(nums, expected_result):
    assert sol.findMaxConsecutiveOnes(nums) == expected_result


@pytest.mark.parametrize('expected_exception, nums',
                         [(ValueError, []),
                          (ValueError, [1] * (10**5 + 1)),
                          (ValueError, [0] * (10**5 + 1)),
                          (ValueError, [1, 1, 1, 2, 3, 1, 0, 0]),
                          (ValueError, [1, 0, 0, 1, 'aaa', '1', 0])])
def test_errors(expected_exception, nums):
    with pytest.raises(expected_exception):
        sol.findMaxConsecutiveOnes(nums)
