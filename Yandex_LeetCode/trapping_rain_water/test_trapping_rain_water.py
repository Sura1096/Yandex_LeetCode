import pytest
from trapping_rain_water import Solution


sol = Solution()


@pytest.mark.parametrize('height, expected_result',
                         [([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
                          ([4, 2, 0, 3, 2, 5], 9),
                          ([3, 0, 2, 0, 4], 7),
                          ([4, 1, 3, 0, 5], 8),
                          ([5, 1, 0, 1, 3, 4, 2, 1, 2], 12),
                          ([0, 1, 0, 2, 0, 3, 0, 4], 6)])
def test_positive_cases(height, expected_result):
    assert sol.trap(height) == expected_result


@pytest.mark.parametrize('height, expected_result',
                         [([1], 0),
                          ([0, 0, 0, 0], 0),
                          ([1, 2, 3, 4, 5], 0),
                          ([2, 2], 0),
                          ([2, 0, 2], 2)])
def test_boundary_cases(height, expected_result):
    assert sol.trap(height) == expected_result


@pytest.mark.parametrize('expected_exception, height',
                         [(ValueError, []),
                          (ValueError, [2] * 3 * 10**4),
                          (TypeError, [1, 2, 0, 5, 'a', 9, 1]),
                          (ValueError, [8, 1, -1, 4, 1]),
                          (ValueError, [1, 2, 3, 4, 5*10**5])])
def test_errors(expected_exception, height):
    with pytest.raises(expected_exception):
        sol.trap(height)
