from typing import List


'''
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        L = T = 0
        R = B = n - 1
        ans = 1

        while L <= R:
            # Fill top row
            for col in range(L, R + 1):
                matrix[T][col] = ans
                ans += 1
            T += 1

            # Fill right column
            for r in range(T, B + 1):
                matrix[r][R] = ans
                ans += 1
            R -= 1

            # Fill bottom (reverse order)
            for col in range(R, L - 1, -1):
                matrix[B][col] = ans
                ans += 1
            B -= 1

            # Fill left column (reverse order)
            for l in range(B, T - 1, -1):
                matrix[l][L] = ans
                ans += 1
            L += 1

        return matrix


ins = Solution()
print(ins.generateMatrix(3))
print(ins.generateMatrix(4))
print(ins.generateMatrix(1))