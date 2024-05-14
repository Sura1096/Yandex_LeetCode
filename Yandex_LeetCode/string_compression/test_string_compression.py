import pytest
from string_compression import Solution


sol = Solution()


@pytest.mark.parametrize('chars, expected_result',
                         [(["a", "a", "b", "b", "c"], 5),
                          (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4),
                          (['a', 'a', 'b', 'b', 'b', 'a', 'a', 'c', 'c'], 8),
                          (['1', '1', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '5', '6', '6'], 10),
                          (["a", "a", "a", "b", "b", "a", "a"], 6)])
def test_positive_cases(chars, expected_result):
    assert sol.compress(chars) == expected_result


@pytest.mark.parametrize('chars, expected_result',
                         [(["a"], 1),
                          (["a", "a", "a", "a", "a"], 2),
                          ([" ", " ", "a", "a", "a"], 4)])
def test_boundary_cases(chars, expected_result):
    assert sol.compress(chars) == expected_result


@pytest.mark.parametrize('expected_exception, chars',
                         [(ValueError, []),
                          (ValueError, ["a"] * 2001)])
def test_errors(expected_exception, chars):
    with pytest.raises(expected_exception):
        sol.compress(chars)
