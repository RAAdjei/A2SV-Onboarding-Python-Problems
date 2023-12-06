class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def inbound(r, c):
            return (0 <= r < len(grid) and 0 <= c < len(grid[0]))

        def dfs(r, c,):
            if not inbound(r, c):
                return 0
            if grid[r][c] == "0":
                return 0

            if (r, c) in visited:
                return 0

            visited.add((r, c))

            dfs(r, c-1)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r+1, c)

            return 1

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if dfs(row, col):
                    count += 1

        return count
"""
Time - O(N^2)
space - O(N)
"""


        
        
