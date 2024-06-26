import pytest
from merge_intervals import Solution


sol = Solution()


@pytest.mark.parametrize('intervals, expected_result',
                         [([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
                          ([[1, 4], [4, 5]], [[1,5]]),
                          ([[2, 167], [7, 10], [9, 12], [4, 19], [1, 56]], [[1, 167]]),
                          ([[1, 2], [3, 4], [5, 6], [10, 11], [12, 13]], [[1, 2], [3, 4], [5, 6], [10, 11], [12, 13]])])
def test_positive_cases(intervals, expected_result):
    assert sol.merge(intervals) == expected_result


@pytest.mark.parametrize('intervals, expected_result',
                         [([[1, 3]], [[1, 3]]),
                          ([[0, 0], [0, 0]], [[0, 0]])])
def test_boundary_cases(intervals, expected_result):
    assert sol.merge(intervals) == expected_result


@pytest.mark.parametrize('expected_exception, intervals',
                         [(ValueError, []),
                          (ValueError, [[1, 2, 3], [1, 2], [2, 3]]),
                          (ValueError, [[1, 2], [2, 3], [-1, 0]]),
                          (ValueError, [[1, 2], [7, 10], [9, 4]])])
def test_errors(expected_exception, intervals):
    with pytest.raises(expected_exception):
        sol.merge(intervals)
