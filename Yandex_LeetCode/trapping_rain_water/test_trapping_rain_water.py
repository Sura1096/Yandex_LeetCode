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
