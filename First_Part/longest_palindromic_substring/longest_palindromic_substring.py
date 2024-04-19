'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''


class Solution:
    def longestPalindom(self, s: str) -> str:
        if len(s) < 1 or len(s) > 1000:
            raise ValueError('Input length must be 1 <= length <= 1000.')
        if not s.isalnum():
            raise ValueError('Input must consist of digits and English letters only.')

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ''
        for i in range(len(s)):
            substring1 = expand(i, i)
            if len(substring1) > len(result):
                result = substring1
            substring2 = expand(i, i+1)
            if len(substring2) > len(result):
                result = substring2

        return result


if __name__ == '__main__':
    sol = Solution()
    s = 'xabax'
    print(sol.longestPalindom(s))