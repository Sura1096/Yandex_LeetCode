from typing import List


'''
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) < 1 or len(nums) > 10**5:
            raise ValueError('Input length must be 1 <= length <= 10^5')
        if k < 0 or k > len(nums):
            raise ValueError('K value must be 0 <= k <= list.length')

        for num in nums:
            if num not in (0, 1):
                raise ValueError('Item value in a list must be either 0 or 1')
        left, maxi, zeroes = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                while zeroes >= k:
                    if nums[left] == 0:
                        zeroes -= 1
                    left += 1
                zeroes += 1
            maxi = max(right - left + 1, maxi)

        return maxi


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(obj.longestOnes(nums, k))

    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(obj.longestOnes(nums, k))

    nums = [1, 1, 1, 0, 0, 1, 1, 0]
    k = 3
    print(obj.longestOnes(nums, k))
