'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > (5 * (10**4)):
            raise ValueError('Input length must be length <= 5 * 10^4')
        left = 0
        hash_table = {}
        longest_substring = 0

        for right, char in enumerate(s):
            if char in hash_table and hash_table[char] >= left:
                left = hash_table[char] + 1
            hash_table[char] = right
            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring


if __name__ == '__main__':
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))

    s = "bbbbbbb"
    print(sol.lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))