class Solution:
    def handleSingleRow(self, rowNum: int, boxGrid: List[List[str]], colLen:int):
        j = colLen-1
        while j>=0 and boxGrid[rowNum][j] != ".":
            j -= 1
        i = j-1
        while i>=0 and j>=0:
            if boxGrid[rowNum][j] == "." and boxGrid[rowNum][i] == "#":
                boxGrid[rowNum][j] = "#"
                boxGrid[rowNum][i] = "."
                j -= 1
            elif boxGrid[rowNum][i] == "*":
                j = i-1
                while j>=0 and boxGrid[rowNum][j] != ".":
                    j-=1
                    i = j
            
            i -= 1
        
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        res = [["."]*len(boxGrid) for i in range(len(boxGrid[0]))]
        rowLen = len(boxGrid)
        colLen = len(boxGrid[0])

        #handle each row in the main matrix then copy to the result matrx
        for rowNum in range(rowLen):
            self.handleSingleRow(rowNum, boxGrid, colLen)
        
        for i in range(rowLen):
            for j in range(colLen):
                res[j][rowLen-i-1] = boxGrid[i][j]
        
        return res