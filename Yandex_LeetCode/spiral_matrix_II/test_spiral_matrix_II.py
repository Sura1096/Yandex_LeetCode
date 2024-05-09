import pytest
from spiral_matrix_II import Solution


sol = Solution()


@pytest.mark.parametrize('n, expected_result',
                         [(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
                          (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
                          (2, [[1, 2], [4, 3]]),
                          (5, [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8],
                               [13, 12, 11, 10, 9]])])
def test_positive_cases(n, expected_result):
    assert sol.generateMatrix(n)


@pytest.mark.parametrize('n, expected_result',
                         [(1, [[1]])])
def test_boundary_cases(n, expected_result):
    assert sol.generateMatrix(n)


@pytest.mark.parametrize('expected_exception, n',
                         [(ValueError, 0),
                          (ValueError, -1),
                          (ValueError, 21),
                          (ValueError, 'a')])
def test_errors(expected_exception, n):
    with pytest.raises(expected_exception):
        sol.generateMatrix(n)
