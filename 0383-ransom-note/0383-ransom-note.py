class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0]*26
        for i in magazine :
            arr[ord(i)-ord("a")] = arr[ord(i)-ord("a")]+1
        for j in ransomNote:
            arr[ord(j)-ord("a")] = arr[ord(j)-ord("a")]-1
        return False if any(i<0 for i in arr) else True