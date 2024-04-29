import pytest
from maximize_distance_to_closest_person import Solution


sol = Solution()


@pytest.mark.parametrize('seats, expected_result',
                         [([1, 0, 0, 0, 1, 0, 1], 2),
                          ([1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 6),
                          ([0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0], 3)])
def test_positive_cases(seats, expected_result):
    assert sol.maxDistToClosest(seats) == expected_result


@pytest.mark.parametrize('seats, expected_result',
                         [([1, 0], 1),
                          ([1, 0, 0, 0], 3),
                          ([1, 1, 1, 1, 1, 0], 1),
                          ([0, 0, 0, 0, 0, 0, 0, 0, 1], 8)])
def test_boundary_cases(seats, expected_result):
    assert sol.maxDistToClosest(seats) == expected_result
