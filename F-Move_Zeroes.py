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
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
'''


class Solution:
    def moveZeroes(self, nums: List[int]):
        piv = 0

        for i in range(1, len(nums)):
            if nums[i] != 0 and nums[piv] == 0:
                nums[piv], nums[i] = nums[i], nums[piv]

            if nums[piv] != 0:
                piv += 1

        return nums


sol = Solution()
print(sol.moveZeroes([0, 1, 0, 3, 12]))
print(sol.moveZeroes([0]))
print(sol.moveZeroes([0, 0, 0, 1, 0, 3, 12, 0]))
print(sol.moveZeroes([1, 2, 4, 0, 3, 0, 12, 0]))
ls = [randint(0, 6) for i in range(10)]
print(ls)
print(sol.moveZeroes(ls))