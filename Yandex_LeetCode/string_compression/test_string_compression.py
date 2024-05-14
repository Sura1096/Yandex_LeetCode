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
