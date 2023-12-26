from typing import List


'''
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []
        pointer = intervals[0]
        for ind in range(1, len(intervals)):
            if intervals[ind][0] <= pointer[1]:
                pointer[1] = max(pointer[1], intervals[ind][1])
            else:
                result.append(pointer)
                pointer = intervals[ind]
        result.append(pointer)

        return result


sol = Solution()
interval1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(sol.merge(interval1))

interval2 = [[1, 4], [4, 5]]
print(sol.merge(interval2))