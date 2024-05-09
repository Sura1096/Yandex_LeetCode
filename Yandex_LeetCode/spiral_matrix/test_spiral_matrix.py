import pytest
from spiral_matrix import Solution


sol = Solution()


@pytest.mark.parametrize('matrix, expected_result',
                         [([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
                          ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
                          ([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], [1, 2, 4, 6, 8, 10, 9, 7, 5, 3])])
def test_positive_numbers(matrix, expected_result):
    assert sol.spiralOrder(matrix) == expected_result


@pytest.mark.parametrize('matrix, expected_result',
                         [([[1], [4]], [1, 4]),
                          ([[1, 2]], [1, 2]),
                          ([[1], [4], [6]], [1, 4, 6]),
                          ([[1]], [1])])
def test_boundary_cases(matrix, expected_result):
    assert sol.spiralOrder(matrix) == expected_result


@pytest.mark.parametrize('matrix, expected_result',
                         [([[-10, -9], [-8, -7], [-6, -5], [-4, -3]], [-10, -9, -7, -5, -3, -4, -6, -8]),
                          ([[-5], [-4], [-3], [-2], [-1], [0]], [-5, -4, -3, -2, -1, 0]),
                          ([[0]], [0])])
def test_negative_numbers(matrix, expected_result):
    assert sol.spiralOrder(matrix) == expected_result


@pytest.mark.parametrize('expected_exception, matrix',
                         [(ValueError, []),
                          (ValueError, [[1] * 11]),
                          (ValueError, [[2]] * 11),
                          (ValueError, [[]]),
                          (ValueError, [[-101, -100], [-99, -98]]),
                          (ValueError, [[99, 100], [101, 102]])])
def test_errors(expected_exception, matrix):
    with pytest.raises(expected_exception):
        sol.spiralOrder(matrix)
