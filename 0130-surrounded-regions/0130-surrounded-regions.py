class Solution:
    def dfs(self, board, row, col):
        if row<0 or col<0 or row >= len(board) or col >= len(board[0]) or board[row][col] != "O":
            return
        board[row][col] = "S"
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for r, c in directions:
            self.dfs(board,  row + r, col + c)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #row change
        for i in range(len(board)):
            #column same
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            if board[i][len(board[0]) - 1] == "O":
                self.dfs(board, i, len(board[0]) - 1)
            
        #column change
        for i in range(len(board[0])):
            #row same
            if board[len(board)-1][i] == "O":
                self.dfs(board, len(board)-1, i)
            if board[0][i] == "O":
                self.dfs(board, 0, i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"

        