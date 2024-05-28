from typing import List


'''
974. Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0

Constraints:
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
2 <= k <= 10^4
'''


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        if len(nums) < 1 or len(nums) > 3 * 10**4:
            raise ValueError('Length of the nums list must be 1 <= nums.length <= 3 * 10^4')
        if not isinstance(k, int):
            raise TypeError('Value of k variable must be an integer')
        if k < 2 or k > 10**4:
            raise ValueError('Value of k variable must be 2 <= k <= 10^4')
        for num in nums:
            if not isinstance(num, int):
                raise TypeError('Value of an item in a list must be an integer')
            if num < -10**4 or num > 10**4:
                raise ValueError('Value of an item in a list must be -10^4 <= nums[i] <= 10^4')

        prefix_sum = 0
        subarray_count = 0
        dct = {0: 1}

        for num in nums:
            prefix_sum += num
            reminder = prefix_sum % k
            if reminder in dct:
                subarray_count += dct[reminder]
            dct[reminder] = dct.get(reminder, 0) + 1

        return subarray_count


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(sol.subarraysDivByK(nums, k))
