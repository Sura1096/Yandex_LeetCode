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
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


class Solution:
    def sort_str(self, string):
        lst = [char for char in string]

        for i in range(len(lst) - 1):
            for j in range(len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    temp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = temp

        return ''.join(lst)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for item in strs:
            dct[self.sort_str(item)] = dct.get(self.sort_str(item), []) + [item]

        lst = []
        for value in dct.values():
            lst.append(value)

        return lst


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))