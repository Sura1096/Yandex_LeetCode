from typing import List


'''
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] 
longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

Explanation:
We are not modifying the given array. The terms "remove" and "delete" are used in the context of our sliding window, 
not the original array.
The array itself remains unchanged. 
The sliding window is just a conceptual tool used in our algorithm to examine a subset of the array. 
As we move the window through the array (by adjusting our pointers), some elements will fall outside the window, 
but they are not removed from the array.
'''


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) < 1 or len(nums) > (10**5):
            raise ValueError('The length of an input data must be 1 <= length <= 10^5.')
        for item in nums:
            if item not in (0, 1):
                raise ValueError('The item in nums must be either 0 or 1.')
        longest_subarray = 0
        left = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            longest_subarray = max(longest_subarray, right - left)
        return longest_subarray


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 0, 1]
    print(sol.longestSubarray(nums))

    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(sol.longestSubarray(nums))

    nums = [1, 1, 1]
    print(sol.longestSubarray(nums))