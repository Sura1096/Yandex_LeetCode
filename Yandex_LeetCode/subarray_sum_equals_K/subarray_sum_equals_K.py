from typing import List


'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

Hints:
1. Will Brute force work here? Try to optimize it.
2. Can we optimize it by using some extra space?
3. What about storing sum frequencies in a hash table? Will it be useful?
4. sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. 
Can we use this property to optimize it.
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < 1 or len(nums) > 2 * 10**4:
            raise ValueError('Input length must be 1 <= nums.length <= 2 * 10^4')
        if not isinstance(k, int):
            raise TypeError('Value of the variable k must be an integer')
        if k < -10**7 or k > 10**7:
            raise ValueError('Value of the variable k must be -10^7 <= k <= 10^7')

        for num in nums:
            if not isinstance(num, int):
                raise TypeError('Value of an item in a list must be an integer')
            if num < -1000 or num > 1000:
                raise ValueError('Value of an item in a list must be -1000 <= nums[i] <= 1000')

        prefix = 0
        count = 0
        dct = {0: 1}

        for num in nums:
            prefix += num

            if prefix - k in dct:
                count += dct[prefix - k]

            if prefix not in dct:
                dct[prefix] = 1

            else:
                dct[prefix] += 1

        return count


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1]
    k = 2
    print(sol.subarraySum(nums, k))

    nums = [1, 2, 3]
    k = 3
    print(sol.subarraySum(nums, k))

    nums = [-1, -1, -2, -2, -2, 4, 2, 2, 3]
    k = 6
    print(sol.subarraySum(nums, k))