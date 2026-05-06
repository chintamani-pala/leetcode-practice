class Solution:
    def handleSingleRow(self, box, row):
        j = len(box[row]) - 1

        for i in range(len(box[row]) - 1, -1, -1):

            if box[row][i] == "*":
                j = i - 1

            elif box[row][i] == "#":

                box[row][i] = "."
                box[row][j] = "#"
                j -= 1
        
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        arr = [["."]*len(boxGrid) for i in range(len(boxGrid[0]))]
        for i in range(len(boxGrid)):
            self.handleSingleRow(boxGrid, i)
        
        for i in range(len(boxGrid)):
            for j in range(len(boxGrid[0])):
                arr[j][i] = boxGrid[i][j]
        return [it[::-1] for it in arr]