from typing import List


'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bin_search(nums, target, True)
        right = self.bin_search(nums, target, False)
        return [left, right]

    def bin_search(self, nums: List[int], target: int, leftBias: bool):
        start = 0
        end = len(nums) - 1
        i = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                i = mid
                if leftBias:
                    end = mid - 1
                else:
                    start = mid + 1
        return i


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.searchRange(nums, target))

    nums = [5, 7, 7, 8, 8, 10]
    target = 9
    print(sol.searchRange(nums, target))

    nums = [4, 5, 8, 8, 8, 9, 10]
    target = 8
    print(sol.searchRange(nums, target))