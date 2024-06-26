from typing import List


'''
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) < 1 or len(nums) > 10**4:
            raise ValueError('Input data length must be 1 <= length <= 10^4')
        if len(set(nums)) < len(nums):
            raise ValueError('All the numbers of nums must be unique.')
        for num in nums:
            if num < 0 or num > len(nums):
                raise ValueError('Item value must be 0 <= nums[i] <= length')
        dct = {}
        for el in nums:
            dct[el] = 0

        for i in range(len(nums) + 1):
            if i not in dct:
                return i


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 0, 1]
    print(sol.missingNumber(nums))

    nums = [0, 1]
    print(sol.missingNumber(nums))

    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(sol.missingNumber(nums))