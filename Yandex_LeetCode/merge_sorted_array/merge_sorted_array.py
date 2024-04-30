from typing import List


'''
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. 
The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) != m + n:
            raise ValueError('Length of nums1 must be nums1.length == m + n')
        if len(nums2) != n:
            raise ValueError('Length of nums2 must be nums2.length == n')
        if m < 0 or m > 200 or n < 0 or n > 200:
            raise ValueError('Value of m/n must be 0 <= m, n <= 200')
        if m + n < 1 or m + n > 200:
            raise ValueError('Value of m + n must be 1 <= m + n <= 200')
        for num in nums1:
            if num < -10**9 or num > 10**9:
                raise ValueError('Value of an item in nums1 must be -10^9 <= nums1[i] <= 10^9')
        for num in nums2:
            if num < -10**9 or num > 10**9:
                raise ValueError('Value of an item in nums2 must be -10^9 <= nums2[i] <= 10^9')
        i = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[i] = nums2[n - 1]
                n -= 1
            else:
                nums1[i] = nums1[m - 1]
                m -= 1
            i -= 1
        while n > 0:
            nums1[i] = nums2[n - 1]
            n -= 1
            i -= 1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(sol.merge(nums1, m, nums2, n))

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(sol.merge(nums1, m, nums2, n))

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(sol.merge(nums1, m, nums2, n))