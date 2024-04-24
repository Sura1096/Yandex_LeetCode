from typing import List


'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = 0
        for i in range(len(height)):
            if height[i] > height[max_height]:
                max_height = i

        result = 0
        left = 0
        for right in range(max_height):
            if left < height[right]:
                left = height[right]
            result += left - height[right]

        left = 0
        for right in range(len(height) - 1, max_height, -1):
            if left < height[right]:
                left = height[right]
            result += left - height[right]

        return result


if __name__ == '__main__':
    sol = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(sol.trap(height))

    height = [4, 2, 0, 3, 2, 5]
    print(sol.trap(height))

    height = [1]
    print(sol.trap(height))