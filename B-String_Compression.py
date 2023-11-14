from typing import List


'''
443. String Compression

Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

Hints:
How do you know if you are at the end of a consecutive group of characters?
'''


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        s = ''
        start = 0

        for i in range(1, len(chars)):
            if chars[start] != chars[i]:
                if i - start > 1:
                    s += chars[start] + str(i - start)
                elif i - start == 1:
                    s += chars[start]
                start = i
            if i == len(chars) - 1:
                if i - start >= 1:
                    s += chars[start] + str(i - start+1)
                elif i - start == 0:
                    s += chars[start]
        for i in range(len(s)):
            chars[i] = s[i]

        return len(chars[:len(s)])


sol = Solution()
print(sol.compress(["a"]))
print(sol.compress(["a", "a", "b", "b", "c"]))
print(sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(sol.compress(['a', 'a', 'b', 'b', 'b', 'a', 'a', 'c', 'c']))
print(sol.compress(['1', '1', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '5', '6',
                    '6']))
print(sol.compress(["a", "a", "a", "b", "b", "a", "a"]))