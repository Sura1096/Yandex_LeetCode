from typing import List


'''
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) < 1 or len(nums) > 10**4:
            raise ValueError('Input length must be 1 <= nums.length <= 10^4')
        for num in nums:
            if num < -10**4 or num > 10**4:
                raise ValueError('Item value must be -10^4 <= nums[i] <= 10^4')
        dp = [0] * len(nums)
        start = 0
        end = len(nums) - 1
        i = end

        while start <= end:
            if abs(nums[start]) <= abs(nums[end]):
                dp[i] = nums[end] ** 2
                end -= 1
            elif abs(nums[start]) > abs(nums[end]):
                dp[i] = nums[start] ** 2
                start += 1
            i -= 1

        return dp


if __name__ == '__main__':
    sol = Solution()
    nums_list = [-4, -1, 0, 3, 10]
    print(sol.sortedSquares(nums_list))

    nums_list = [-7, -3, 2, 3, 11]
    print(sol.sortedSquares(nums_list))