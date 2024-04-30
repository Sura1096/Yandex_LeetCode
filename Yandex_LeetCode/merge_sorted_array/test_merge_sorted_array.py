import pytest
from merge_sorted_array import Solution


sol = Solution()


@pytest.mark.parametrize('nums1, m, nums2, n, expected_result',
                         [([1, 2, 3, 0, 0, 0], 3,
                           [2, 5, 6], 3,
                           [1, 2, 2, 3, 5, 6]),
                          ([1, 3, 5, 0, 0, 0], 3,
                           [2, 4, 6], 3,
                           [1, 2, 3, 4, 5, 6]),
                          ([0, 0, 0], 0,
                           [1, 2, 3], 3,
                           [1, 2, 3]),
                          ([4, 5, 6, 7, 0, 0, 0], 4,
                           [1, 2, 3], 3,
                           [1, 2, 3, 4, 5, 6, 7])])
def test_positive_cases(nums1, m, nums2, n, expected_result):
    assert sol.merge(nums1, m, nums2, n) == expected_result
