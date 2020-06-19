class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in grid[i]:
                if j < 0:
                    result += 1
        return result
