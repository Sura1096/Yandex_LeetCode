import pytest
from valid_palindrome import Solution


sol = Solution()


@pytest.mark.parametrize('s, expected_result', [('A man, a plan, a canal: Panama', True),
                                                ("Was it a car or a cat I saw?", True),
                                                ("Able was I ere I saw Elba", True)])
def test_is_palindromes(s, expected_result):
    assert sol.isPalindrome(s) == expected_result


@pytest.mark.parametrize('s, expected_result', [("race a car", False),
                                                ("hello world", False),
                                                ("1234567890", False)])
def test_not_palindromes(s, expected_result):
    assert sol.isPalindrome(s) == expected_result


@pytest.mark.parametrize('s, expected_result', [("z", True),
                                                (" ", True),
                                                ('aaaaa', True)])
def test_boundary_cases(s, expected_result):
    assert sol.isPalindrome(s) == expected_result


@pytest.mark.parametrize('expected_exception, s', [(ValueError, 'A' * (3 * (10**5))),
                                                   (ValueError, '')])
def test_performance(expected_exception, s):
    with pytest.raises(expected_exception):
        sol.isPalindrome(s)