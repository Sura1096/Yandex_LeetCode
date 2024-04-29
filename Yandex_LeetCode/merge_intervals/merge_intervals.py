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
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1 or len(intervals) > 10**4:
            raise ValueError('Input length must be 1 <= length <= 10^4')
        for item in intervals:
            if len(item) != 2:
                raise ValueError('Item length of a list must be equal to 2')
            if item[0] < 0 or item[0] > 10**4:
                raise ValueError('Start position must have value 0 <= start <= 10^4')
            if item[1] < item[0] or item[1] > 10**4:
                raise ValueError('End position must have value start <= end <= 10^4')
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


if __name__ == '__main__':
    sol = Solution()
    interval1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(sol.merge(interval1))

    interval2 = [[1, 4], [4, 5]]
    print(sol.merge(interval2))