from typing import List


'''
228. Summary Ranges

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:
0 <= nums.length <= 20
-2^31 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
'''


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        else:
            new_list = [[nums[0]]]
            i = 0

            for ind in range(1, len(nums)):
                if nums[ind] - nums[ind - 1] == 1:
                    new_list[i].append(nums[ind])
                else:
                    new_list.append([nums[ind]])
                    i += 1

            for j in range(len(new_list)):
                if new_list[j][0] != new_list[j][-1]:
                    new_list[j] = str(new_list[j][0]) + '->' + str(new_list[j][-1])
                else:
                    new_list[j] = str(new_list[j][0])

            return new_list


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    print(sol.summaryRanges(nums))

    nums = [0, 2, 3, 4, 6, 8, 9]
    print(sol.summaryRanges(nums))

    nums = [0, 1, 2, 3, 4]
    print(sol.summaryRanges(nums))

    nums = [0]
    print(sol.summaryRanges(nums))

    nums = []
    print(sol.summaryRanges(nums))

    nums = [-2147483648, -2147483647, 2147483647]
    print(sol.summaryRanges(nums))
