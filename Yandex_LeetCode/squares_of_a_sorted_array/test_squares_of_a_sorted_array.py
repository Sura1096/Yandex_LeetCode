import pytest
from squares_of_a_sorted_array import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
                          ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
                          ([-10, -4, -1, 11], [1, 16, 100, 121])])
def test_positive_cases(nums, expected_result):
    assert sol.sortedSquares(nums) == expected_result


@pytest.mark.parametrize('nums, expected_result',
                         [([-4], [16]),
                          ([2, 3, 11], [4, 9, 121]),
                          ([-10, -4, -1, 10, 11], [1, 16, 100, 100, 121]),
                          ([7], [49])])
def test_boundary_cases(nums, expected_result):
    assert sol.sortedSquares(nums) == expected_result
