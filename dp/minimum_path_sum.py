from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid[0])
        height = len(grid)

        if row == 1 and height == 1:
            return grid[0][0]

        sub_array = [grid[0][0]]

        for i in range(height):
            for j in range(row):
                if i == 0 and j == 0:
                    continue

                a = i * row + j

                if i < 1:
                    sub_array.append(sub_array[a - 1] + grid[i][j])
                    continue
                if a % row == 0:
                    sub_array.append(sub_array[a-row] + grid[i][j])
                else:
                    minS = min(sub_array[a - 1], sub_array[a-row])
                    sub_array.append(minS+ grid[i][j])

        return sub_array[-1]

s = Solution()
print(s.minPathSum(grid = [[1,2,3],[4,5,6]]))

