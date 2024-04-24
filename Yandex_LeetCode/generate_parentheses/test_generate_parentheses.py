import pytest
from generate_parentheses import Solution


sol = Solution()


@pytest.mark.parametrize('n, expected_result', [(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
                                                (1, ["()"]),
                                                (2, ['(())', '()()'])])
def test_positive_cases(n, expected_result):
    assert sol.generateParentheses(n) == expected_result


@pytest.mark.parametrize('expected_exception, n', [(ValueError, 0),
                                                   (ValueError, -1),
                                                   (ValueError, 9),
                                                   (TypeError, 'a')])
def test_errors(expected_exception, n):
    with pytest.raises(expected_exception):
        sol.generateParentheses(n)
