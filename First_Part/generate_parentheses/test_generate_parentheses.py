import unittest
from generate_parentheses import Solution


class TestGenerateParentheses(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_generate_parentheses(self):
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


if __name__ == '__main__':
    unittest.main()