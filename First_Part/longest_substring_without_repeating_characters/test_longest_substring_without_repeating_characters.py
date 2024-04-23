import pytest
from longest_substring_without_repeating_characters import Solution


sol = Solution()


@pytest.mark.parametrize('s, expected_result',
                         [("abcabcbb", 3),
                          ("pwwkew", 3),
                          ("agbfaacccvccdbhhnjfhhcvvvg", 4)])
def test_positive_cases(s, expected_result):
    assert sol.lengthOfLongestSubstring(s) == expected_result


@pytest.mark.parametrize('s, expected_result',
                         [("bbbbbbbbbb", 1),
                          ("", 0),
                          ("a", 1),
                          ("abca bcbb", 4),
                          ("ab cab cb b", 4),
                          ("asdfghj", 7)])
def test_boundary_cases(s, expected_result):
    assert sol.lengthOfLongestSubstring(s) == expected_result
