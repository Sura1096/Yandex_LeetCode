import pytest
from longest_palindromic_substring import Solution


sol = Solution()


@pytest.mark.parametrize('s, expected_result',
                         [("babad", "bab"),
                          ("cbbd", "bb"),
                          ("acvb", "a"),
                          ("xabax", "xabax"),
                          ("xabay", "aba")])
def test_positive(s, expected_result):
    assert sol.longestPalindom(s) == expected_result
