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


@pytest.mark.parametrize('nums, expected_result',
                         [([1], 0),
                          ([0], 1)])
def test_boundary_cases(nums, expected_result):
    assert sol.missingNumber(nums) == expected_result


@pytest.mark.parametrize('expected_exception, nums',
                         [(ValueError, []),
                          (ValueError, [i for i in range(10**4 + 3)]),
                          (ValueError, [0, 1, 2, 3, 3, 4]),
                          (ValueError, [1, 2, 3, -1, 0]),
                          (ValueError, [3, 4, 5])])
def test_errors(expected_exception, nums):
    with pytest.raises(expected_exception):
        sol.missingNumber(nums)
