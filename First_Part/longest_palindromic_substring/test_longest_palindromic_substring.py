import pytest
from longest_palindromic_substring import Solution


sol = Solution()


@pytest.mark.parametrize('s, expected_result',
                         [("babad", "bab"),
                          ("cbbd", "bb"),
                          ("xabax", "xabax"),
                          ("xabay", "aba"),
                          ('123ffdgh12455421', '12455421')])
def test_positive(s, expected_result):
    assert sol.longestPalindom(s) == expected_result


@pytest.mark.parametrize('s, expected_result',
                         [('andfgh', 'a'),
                          ('a', 'a'),
                          ('asdfghjkl', 'a'),
                          ('ad123dfgd', 'a'),
                          ('1234dfg', '1')])
def test_boundary_cases(s, expected_result):
    assert sol.longestPalindom(s) == expected_result
