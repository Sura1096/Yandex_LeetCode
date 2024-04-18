import pytest
from group_anagrams import Solution


sol = Solution()


@pytest.mark.parametrize('string, expected_result',
                         [(["eat", "tea", "tan", "ate", "nat", "bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
                          ([''], [['']]),
                          (['a'], [['a']])])
def test_positive_cases(string, expected_result):
    assert sol.groupAnagrams(string) == expected_result


@pytest.mark.parametrize('expected_exception, string',
                         [(ValueError, []),
                          (ValueError, ['abc'] * ((10**4) + 1)),
                          (ValueError, ["eat", "tea" * 101, "tan", "ate", "nat", "bat"])])
def test_errors(expected_exception, string):
    with pytest.raises(expected_exception):
        sol.groupAnagrams(string)
