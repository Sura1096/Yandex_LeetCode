import pytest
from perfect_squares import Solution


sol = Solution()


@pytest.mark.parametrize('n, expected_result',
                         [(12, 3),
                          (13, 2),
                          (15, 4),
                          (132, 3)])
def test_positive_cases(n, expected_result):
    assert sol.numSquares(n) == expected_result
