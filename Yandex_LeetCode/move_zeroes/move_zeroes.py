from typing import List


'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0

        for cur_ind in range(len(nums)):
            if nums[cur_ind] != 0:
                nums[pointer], nums[cur_ind] = nums[cur_ind], nums[pointer]
                pointer += 1


sol = Solution()
print(sol.moveZeroes([0, 1, 0, 3, 12]))
print(sol.moveZeroes([0]))
print(sol.moveZeroes([0, 0, 0, 1, 0, 3, 12, 0]))
print(sol.moveZeroes([1, 2, 4, 0, 3, 0, 12, 0]))