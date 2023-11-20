from typing import List


'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''


class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        result = []
        stack = []

        def generator(open_par, close_par):
            if open_par == close_par == n:
                result.append(''.join(stack))
                return
            if open_par < n:
                stack.append('(')
                generator(open_par+1, close_par)
                stack.pop()
            if close_par < open_par:
                stack.append(')')
                generator(open_par, close_par+1)
                stack.pop()

        generator(0, 0)
        return result


sol = Solution()
print(sol.generateParentheses(3))
