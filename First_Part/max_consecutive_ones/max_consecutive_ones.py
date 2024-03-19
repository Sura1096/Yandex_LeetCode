from typing import List


'''
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            maxi = max(maxi, count)

        return maxi


obj = Solution()
print(obj.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(obj.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
