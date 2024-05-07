from typing import List


'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''


class Solution:
    def rotate(self, matrix: List[List[int]]):
        if len(matrix) < 1 or len(matrix) > 20:
            raise ValueError('Input length must be 1 <= length <= 20')
        for item in matrix:
            if len(item) < len(matrix) or len(item) > len(matrix):
                raise ValueError('Item length in matrix must equal to length of matrix')
            for num in item:
                if num < -1000 or num > 1000:
                    raise ValueError('Each number in item of matrix list must be -1000 <= matrix[i][j] <= 1000')
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # Store the top left value
                temp = matrix[top][left + i]

                # Move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move top left (temp value) into top right
                matrix[top + i][right] = temp
            right -= 1
            left += 1
        return matrix


if __name__ == '__main__':
    sol = Solution()
    print(sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))