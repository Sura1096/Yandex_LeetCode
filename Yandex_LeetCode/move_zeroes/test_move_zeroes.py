import pytest
from move_zeroes import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
                          ([0, 0, 0, 1, 0, 3, 12, 0], [1, 3, 12, 0, 0, 0, 0, 0]),
                          ([1, 2, 4, 0, 3, 0, 12, 0], [1, 2, 4, 3, 12, 0, 0, 0])])
def test_positive_cases(nums, expected_result):
    assert sol.moveZeroes(nums) == expected_result


@pytest.mark.parametrize('nums, expected_result',
                         [([0], [0]),
                          ([12], [12]),
                          ([1, 0], [1, 0])])
def test_boundary_cases(nums, expected_result):
    assert sol.moveZeroes(nums) == expected_result


@pytest.mark.parametrize('expected_exception, nums',
                         [(ValueError, []),
                          (ValueError, [1] * (10**4 + 1)),
                          (ValueError, [1, 2, 3, 0, 0, 4, 'a']),
                          (ValueError, [0, 0, 1, 5 * (-2**31), 2, 0, 4]),
                          (ValueError, [0, 0, 1, 5 * (2**31), 2, 0, 4])])
def test_errors(expected_exception, nums):
    with pytest.raises(expected_exception):
        sol.moveZeroes(nums)
