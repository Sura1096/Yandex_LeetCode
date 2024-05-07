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
