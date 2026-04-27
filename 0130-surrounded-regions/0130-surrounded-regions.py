class Solution:
    # def dfs(self, board, row, col):
    #     if row<0 or col<0 or row >= len(board) or col >= len(board[0]) or board[row][col] != "O":
    #         return
    #     board[row][col] = "S"
    #     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    #     for r, c in directions:
    #         self.dfs(board,  row + r, col + c)
    def dfs(self, vis, board, row, col):
        if board[row][col] == "X":
            return
        if board[row][col] == "O":
            vis[row][col]=1
        directions  = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for r, c in directions:
            nr = row+r
            nc = col+c
            if 0<=nr<len(board) and 0<=nc<len(board[0]) and not vis[nr][nc]:
                self.dfs(vis, board, nr, nc)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # #row change
        # for i in range(len(board)):
        #     #column same
        #     if board[i][0] == "O":
        #         self.dfs(board, i, 0)
        #     if board[i][len(board[0]) - 1] == "O":
        #         self.dfs(board, i, len(board[0]) - 1)
            
        # #column change
        # for i in range(len(board[0])):
        #     #row same
        #     if board[len(board)-1][i] == "O":
        #         self.dfs(board, len(board)-1, i)
        #     if board[0][i] == "O":
        #         self.dfs(board, 0, i)

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == "O":
        #             board[i][j] = "X"
        #         if board[i][j] == "S":
        #             board[i][j] = "O"

        vis = [[0]*len(board[0]) for i in range(len(board))]
        #first row 
        for i in range(len(board[0])):
            self.dfs(vis, board, 0, i)
        #last row
        for i in range(len(board[0])):
            self.dfs(vis, board, len(board)-1, i)
        
        #first col
        for i in range(len(board)):
            self.dfs(vis, board, i, 0)
        
        #last col
        for i in range(len(board)):
            self.dfs(vis, board, i, len(board[0])-1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not vis[i][j] and board[i][j] == "O":
                    board[i][j] = "X"
        

        