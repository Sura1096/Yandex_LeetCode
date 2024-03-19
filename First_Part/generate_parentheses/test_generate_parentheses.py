import unittest
from generate_parentheses import Solution


class TestGenerateParentheses(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_valid_generate_parentheses(self):
        self.assertEqual(
            self.obj.generateParentheses(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"]
        )

        self.assertEqual(
            self.obj.generateParentheses(1),
            ["()"]
        )

        self.assertEqual(
            self.obj.generateParentheses(2),
            ["(())", '()()']
        )

        self.assertEqual(
            self.obj.generateParentheses(4),
            ['(((())))', '((()()))', '((())())',
             '((()))()', '(()(()))', '(()()())',
             '(()())()', '(())(())', '(())()()',
             '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
        )

    def test_invalid_generate_parentheses(self):
        with self.assertRaises(ValueError):
            self.obj.generateParentheses(-1)

        with self.assertRaises(ValueError):
            self.obj.generateParentheses(0)

        with self.assertRaises(ValueError):
            self.obj.generateParentheses(9)


if __name__ == '__main__':
    unittest.main()