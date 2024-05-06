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


@pytest.mark.parametrize('s1, s2, expected_result',
                         [("a", "ab", True),
                          ("c", "a", False),
                          ("abc", "sdfg", False)])
def test_boundary_cases(s1, s2, expected_result):
    assert sol.checkInclusion(s1, s2) == expected_result


@pytest.mark.parametrize('expected_exception, s1, s2',
                         [(ValueError, '', 'a'),
                          (ValueError, 'a', ''),
                          (ValueError, 'abc', 'a'),
                          (ValueError, 'ank1djkf', 'qwertyu'),
                          (ValueError, 'bdjAknf', 'bcfdskjids'),
                          (ValueError, 'asdf', 'jn2dfv'),
                          (ValueError, 'dif', 'lkiXbg'),
                          (ValueError, 'AAA', 'BBB'),
                          (ValueError, '123', '345')])
def test_error_cases(expected_exception, s1, s2):
    with pytest.raises(expected_exception):
        sol.checkInclusion(s1, s2)
