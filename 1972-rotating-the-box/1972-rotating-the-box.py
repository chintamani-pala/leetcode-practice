class Solution:
    def handleSingleRow(self, rowNum: int, boxGrid: List[List[str]]):
        print(rowNum)
        j = len(boxGrid[rowNum])-1
        while j>=0 and boxGrid[rowNum][j] != ".":
            j -= 1
        i = j-1
        while i>=0 and j>=0:
            if boxGrid[rowNum][j] == "." and boxGrid[rowNum][i] == "#":
                print(i, j)
                boxGrid[rowNum][j] = "#"
                boxGrid[rowNum][i] = "."
                j -= 1
            elif boxGrid[rowNum][i] == "*":
                j = i-1
                while j>=0 and boxGrid[rowNum][j] != ".":
                    j-=1
                    i = j
            
            i -= 1
        print(boxGrid[rowNum])
        
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        res = [["."]*len(boxGrid) for i in range(len(boxGrid[0]))]

        #handle each row in the main matrix then copy to the result matrx
        for rowNum in range(len(boxGrid)):
            self.handleSingleRow(rowNum, boxGrid)
        print(boxGrid)
        for i in range(len(boxGrid)):
            for j in range(len(boxGrid[0])):
                res[j][i] = boxGrid[i][j]
        
        return [i[::-1] for i in res]