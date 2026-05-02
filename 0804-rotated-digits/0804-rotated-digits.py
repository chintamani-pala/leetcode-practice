class Solution:
    def isRotated(self, n):
        newn =  ""
        for i in n:
            if i in ["3", "4", "7"]:
                return False
            if i in ["0", "1", "8"]:
                newn+=i
                continue
            if i=="2":
                newn += "5"
            if i=="5":
                newn += "2"
            if i=="6":
                newn+="9"
            if i=="9":
                newn+="6"
        print("newn", newn)
        print("n", n)
        return int(newn) != int(n) 
    def rotatedDigits(self, n: int) -> int:
        ans = []
        for i in range(2,n+1):
            if self.isRotated(str(i)):
                ans.append(i)
        return len(ans)