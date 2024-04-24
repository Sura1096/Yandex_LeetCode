from typing import List


'''
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        nums_sum = nums[0]

        for num in nums[1:]:
            nums_sum = max(num, nums_sum+num)
            max_sum = max(max_sum, nums_sum)

        return max_sum


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(nums))

    nums = [1]
    print(sol.maxSubArray(nums))

    nums = [5, 4, -1, 7, 8]
    print(sol.maxSubArray(nums))