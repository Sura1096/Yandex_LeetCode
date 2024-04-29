from typing import List


'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for first_ind in range(len(nums) - 2):
            if nums[first_ind] > 0:
                break
            elif first_ind > 0 and nums[first_ind] == nums[first_ind - 1]:
                continue
            second_ind = first_ind + 1
            third_ind = len(nums) - 1

            while second_ind < third_ind:
                three_sum = nums[first_ind] + nums[second_ind] + nums[third_ind]
                if three_sum < 0:
                    second_ind += 1
                elif three_sum > 0:
                    third_ind -= 1
                else:
                    triplet = [nums[first_ind], nums[second_ind], nums[third_ind]]
                    answer.append(triplet)
                    while second_ind < third_ind and nums[second_ind] == triplet[1]:
                        second_ind += 1
                    while second_ind < third_ind and nums[third_ind] == triplet[2]:
                        third_ind -= 1
        return answer


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))

    nums = [0, 1, 1]
    print(sol.threeSum(nums))

    nums = [0, 0, 0]
    print(sol.threeSum(nums))