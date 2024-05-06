import pytest
from permutation_in_string import Solution


sol = Solution()


@pytest.mark.parametrize('s1, s2, expected_result',
                         [("ab", "eidbaooo", True),
                          ("ab", "eidaboaoo", True),
                          ("abc", "eidboaooabc", True),
                          ("abc", "eidboaoobac", True)])
def test_positive_cases(s1, s2, expected_result):
    assert sol.checkInclusion(s1, s2) == expected_result


@pytest.mark.parametrize('s1, s2, expected_result',
                         [("ab", "eidboaoo", False),
                          ("abc", "aeidboaooc", False),
                          ("hb", "vchsoakb", False),
                          ("qwerty", "qawsedrftgy", False)])
def test_negative_cases(s1, s2, expected_result):
    assert sol.checkInclusion(s1, s2) == expected_result
