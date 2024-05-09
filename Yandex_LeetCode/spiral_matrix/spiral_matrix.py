from typing import List


'''
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) < 1 or len(matrix) > 10:
            raise ValueError('Input length must be 1 <= matrix.length <= 10')
        for item in matrix:
            if len(item) < 1 or len(item) > 10:
                raise ValueError('Item length in a matrix must be 1 <= matrix[i].length <= 10')
            for num in item:
                if num < -100 or num > 100:
                    raise ValueError('Numbers in a matrix must be -100 <= matrix[i][j] <= 100')
        lst = []
        L = T = 0
        R = len(matrix[0]) - 1
        B = len(matrix) - 1

        while len(lst) < len(matrix) * len(matrix[0]):
            # See all elements at the top
            for t in range(L, R + 1):
                lst.append(matrix[T][t])
            T += 1

            # See all elements from right column
            for r in range(T, B + 1):
                lst.append(matrix[r][R])
            R -= 1

            if T <= B:
                # See all elements at the bottom
                for b in range(R, L - 1, -1):
                    lst.append(matrix[B][b])
                B -= 1

            if L <= R:
                # See all elements from left column
                for l in range(B, T - 1, -1):
                    lst.append(matrix[l][L])
                L += 1

        return lst


if __name__ == '__main__':
    obj = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(obj.spiralOrder(matrix))

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(obj.spiralOrder(matrix))

    matrix = [[1], [4]]
    print(obj.spiralOrder(matrix))

    matrix = [[1, 2]]
    print(obj.spiralOrder(matrix))

    matrix = [[1], [4], [6]]
    print(obj.spiralOrder(matrix))