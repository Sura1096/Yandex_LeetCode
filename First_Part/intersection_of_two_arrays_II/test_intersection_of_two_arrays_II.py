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


@pytest.mark.parametrize('nums1, nums2, expected_result',
                         [([1], [3, 4, 5, 6, 7], []),
                          ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10], []),
                          ([1], [2], []),
                          ([1, 2, 3, 4, 5], [111], [])])
def test_boundary_cases(nums1, nums2, expected_result):
    assert sol.intersect(nums1, nums2) == expected_result


@pytest.mark.parametrize('expected_exception, nums1, nums2',
                         [(ValueError, [0] * 1001, [0, 0]),
                          (ValueError, [0, 0], [1] * 1001),
                          (ValueError, [0] * 1001, [0] * 1001),
                          (ValueError, [], [1, 2]),
                          (ValueError, [1, 2, 3, 4], []),
                          (ValueError, [], []),
                          (ValueError, [1000000, 2, 3, 4, 5], [1, 2, 3]),
                          (ValueError, [1, 2, 3, 4], [1, 4, 5, 600000]),
                          (ValueError, [1, 1, 1, 500000], [5000000, 3, 4, 6])])
def test_errors(expected_exception, nums1, nums2):
    with pytest.raises(expected_exception):
        sol.intersect(nums1, nums2)
