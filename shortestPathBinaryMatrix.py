class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def is_valid(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid) and grid[row][col] == 0)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        # start = (0,0)
        queue = deque([(0, 0, 1)])
        visited = set()
        visited.add((0,0))

        if grid[0][0] == 1:
            return -1

        while queue:
            row, col, lent = queue.popleft() 

            if row == col == len(grid)-1:
                return lent

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, lent + 1))

        return -1
