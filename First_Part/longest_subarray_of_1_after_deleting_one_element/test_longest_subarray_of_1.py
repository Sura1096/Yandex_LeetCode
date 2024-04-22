import pytest
from longest_subarray_of_1_after_deleting_one_element import Solution


sol = Solution()


@pytest.mark.parametrize('nums, expected_result',
                         [([1, 1, 0, 1], 3),
                          ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
                          ([1, 1, 1], 2)])
def test_positive_cases(nums, expected_result):
    assert sol.longestSubarray(nums) == expected_result


@pytest.mark.parametrize('nums, expected_result',
                         [([1], 0),
                          ([0, 0, 0, 0], 0)])
def test_boundary_cases(nums, expected_result):
    assert sol.longestSubarray(nums) == expected_result
