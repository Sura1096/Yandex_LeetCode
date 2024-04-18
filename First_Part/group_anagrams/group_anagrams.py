from typing import List


'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


class Solution:
    def sort_str(self, string):
        lst = [char for char in string]
        lst.sort()

        return ''.join(lst)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1 or len(strs) > 10**4:
            raise ValueError('Input must be greater or equal to 1 and less than or equal to 10^4')
        for el in strs:
            if len(el) > 100:
                raise ValueError('Item in strings must be less than 100')
        dct = {}
        for item in strs:
            dct[self.sort_str(item)] = dct.get(self.sort_str(item), []) + [item]

        lst = []
        for value in dct.values():
            lst.append(value)

        return lst


if __name__ == '__main__':
    sol = Solution()
    string = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(string))

    string2 = [""]
    print(sol.groupAnagrams(string2))

    string3 = ['a']
    print(sol.groupAnagrams(string3))