'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1 or len(s) > 2 * 10**5:
            raise ValueError('Length of input string should be between 1 and 2 * 10^5')
        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s = 'A man, a plan, a canal: Panama'
    print(sol.isPalindrome(s))

    s = 'race a car'
    print(sol.isPalindrome(s))

    s = ' '
    print(sol.isPalindrome(s))
