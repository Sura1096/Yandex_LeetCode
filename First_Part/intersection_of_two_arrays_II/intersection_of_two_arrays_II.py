from typing import List


'''
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into 
the memory at once?
'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < 1 or len(nums1) > 1000:
            raise ValueError('Input list length must be 1 <= length <= 1000')
        if len(nums2) < 1 or len(nums2) > 1000:
            raise ValueError('Input list length must be 1 <= length <= 1000')
        for num in nums1:
            if not isinstance(num, int):
                raise ValueError('Elements in list must be numeric')
            if num < 0 or num > 1000:
                raise ValueError('Number in list must be 0 <= num <= 1000')

        for num in nums2:
            if not isinstance(num, int):
                raise ValueError('Elements in list must be numeric')
            if num < 0 or num > 1000:
                raise ValueError('Number in list must be 0 <= num <= 1000')

        dct = {}
        for el in nums1:
            dct[el] = dct.get(el, 0) + 1

        lst = []
        for el in nums2:
            if el in dct and dct[el] != 0:
                lst.append(el)
                dct[el] = dct[el] - 1

        return lst


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(sol.intersect(nums1, nums2))

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(sol.intersect(nums1, nums2))