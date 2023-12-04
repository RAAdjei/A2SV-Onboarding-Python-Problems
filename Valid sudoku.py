class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or 
                    board[r][c] in boxes[r//3, c//3]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        return True
        
        
        
        
        
        
        
        
        
        
        # lenCol = len(board[0])
        # lenRow = len(board)

      
        # for row in board:
        #     seen = set()
        #     for cell in row:
        #         if cell != ".":
        #             if cell in seen:
        #                 return False
        #             seen.add(cell)

       
        # for col in range(lenCol):
        #     seen = set()
        #     for row in range(lenRow):
        #         cell = board[row][col]
        #         if cell != ".":
        #             if cell in seen:
        #                 return False
        #             seen.add(cell)

        # return True
        
