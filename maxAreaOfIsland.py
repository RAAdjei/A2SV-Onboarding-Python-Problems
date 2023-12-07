class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            count = 1
            count += dfs(r, c-1)
            count += dfs(r, c+1)
            count += dfs(r-1, c)
            count += dfs(r+1, c)

            return count
            
        max_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_count = max(max_count, dfs(row, col))
            
                    

        return max_count

"""
Time - O(N^2)
Space - O(N)
"""


        
