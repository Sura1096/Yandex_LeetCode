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


@pytest.mark.parametrize('n, expected_result',
                         [(1, 1),
                          (4, 1),
                          (9, 1),
                          (100, 1)])
def test_boundary_cases(n, expected_result):
    assert sol.numSquares(n) == expected_result


@pytest.mark.parametrize('expected_exception, n',
                         [(ValueError, 'a'),
                          (ValueError, 0),
                          (ValueError, 6 * 10**4)])
def test_errors(expected_exception, n):
    with pytest.raises(expected_exception):
        sol.numSquares(n)
