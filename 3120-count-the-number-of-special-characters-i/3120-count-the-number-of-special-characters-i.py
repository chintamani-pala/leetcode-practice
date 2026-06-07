class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = [0]*26
        count = 0
        word="".join(list(set(word)))
        for ch in word:
            index=0
            if ch.isupper():
                index = ord(ch)-65
            if ch.islower():
                index= ord(ch)-97
            if seen[index] == 0:
                seen[index] = 1
            else:
                count+=1
                seen[index] = 0
        return count