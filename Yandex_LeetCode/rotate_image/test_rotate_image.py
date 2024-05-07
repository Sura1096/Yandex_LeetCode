import pytest
from rotate_image import Solution


sol = Solution()


@pytest.mark.parametrize('matrix, expected_result',
                         [([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                           [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
                          ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
                           [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
                          ([[3, 5, 7, 9], [1, 2, 3, 4], [12, 13, 14, 15], [6, 8, 17, 11]],
                           [[6, 12, 1, 3], [8, 13, 2, 5], [17, 14, 3, 7], [11, 15, 4, 9]])])
def test_positive_numbers(matrix, expected_result):
    assert sol.rotate(matrix) == expected_result


@pytest.mark.parametrize('matrix, expected_result',
                         [([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
                           [[-7, -4, -1], [-8, -5, -2], [-9, -6, -3]]),
                          ([[-3, -5, -7, -9], [-1, -2, -3, -4], [-12, -13, -14, -15], [-6, -8, -17, -11]],
                           [[-6, -12, -1, -3], [-8, -13, -2, -5], [-17, -14, -3, -7], [-11, -15, -4, -9]])])
def test_negative_numbers(matrix, expected_result):
    assert sol.rotate(matrix) == expected_result


@pytest.mark.parametrize('matrix, expected_result',
                         [([[-1]], [[-1]]),
                          ([[9]], [[9]]),
                          ([[0]], [[0]])])
def test_boundary_cases(matrix, expected_result):
    assert sol.rotate(matrix) == expected_result


@pytest.mark.parametrize('expected_exception, matrix',
                         [(ValueError, []),
                          (ValueError, [[]]),
                          (ValueError, [[1, 2, 3], [1, 2, 3]]),
                          (ValueError, [[1, 2, 3] * 21]),
                          (ValueError, [[1, 2], [3, 4], [5, 6]]),
                          (ValueError, [[1, 2, -10000], [2, 3, 4], [5, 6, 7]]),
                          (ValueError, [[1, 2, 3], [4, 5, 6], [7, 8, 100000]])])
def test_errors(expected_exception, matrix):
    with pytest.raises(expected_exception):
        sol.rotate(matrix)
