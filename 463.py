class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        result = 0
        
        def PerimeterCount(grid):
            count = 0
            for i in range(len(grid)):
                continue1 = 0
                for j in grid[i]:
                    if j == 1:
                        if continue1 == 0:
                            continue1 = 1      
                    else:
                        if continue1 == 1:
                            count += 2
                        continue1 = 0
                if continue1 == 1:
                    count += 2
            return count
        
        result += PerimeterCount(grid)
        grid = list(zip(*grid))
        result += PerimeterCount(grid)
        
        return result
        '''
        
        '''
        h = len(grid)
        w = len(grid[0]) if h else 0
        print(w)
        ans = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j]==1:
                    ans+=4
                    if i>0 and grid[i-1][j]:
                        ans -=2
                    if j>0 and grid[i][j-1]:
                        ans -=2
        return ans
        '''
        m, n = len(grid), len(grid[0])
        self.peri = 0
        
        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 0:
                # visit a water cell from a land cell
                # increment perimeter due to the boundary between these two cells
                self.peri += 1
                return
            elif grid[x][y] == -1:
                # visit a visited land cell
                # nothing happens
                return
            
            grid[x][y] = -1 # mark as visited
            
            # visit from current cell to 4 adjacent cells
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return self.peri
