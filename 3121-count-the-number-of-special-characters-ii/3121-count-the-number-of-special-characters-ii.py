class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #word="".join(list(set(word)))
        charObj={}
        invalidSet=set()
        count=0
        for ch in word:
            if ch.islower():
                if ch not in charObj :
                    charObj[ch]=1
                if charObj[ch] == 0:
                    count-=1
                    charObj[ch.lower()] -= 1
            else:
                ch=ch.lower()
                if ch in charObj and charObj[ch.lower()]==1 and ch not in invalidSet:
                    count+=1
                    charObj[ch.lower()] = 0
                else:
                    invalidSet.add(ch)
                    
                
        return max(0,count)