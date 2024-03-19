'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for el in s:
            if el in pairs:
                stack.append(el)
            elif len(stack) == 0 or el != pairs[stack.pop()]:
                return False

        return len(stack) == 0


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))