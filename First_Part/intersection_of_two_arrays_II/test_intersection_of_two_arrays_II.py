import pytest
from intersection_of_two_arrays_II import Solution


sol = Solution()


@pytest.mark.parametrize('nums1, nums2, expected_result',
                         [([1, 2, 2, 1], [2, 2], [2, 2]),
                          ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
                          ([1], [1, 3, 4, 5, 6], [1]),
                          ([1, 1, 1, 1, 3, 4, 5, 5], [1, 1, 9, 4, 9, 8, 4], [1, 1, 4])])
def test_positive_cases(nums1, nums2, expected_result):
    assert sol.intersect(nums1, nums2) == expected_result
