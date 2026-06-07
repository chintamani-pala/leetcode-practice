class Solution:
    def findLongest(self, hashSet, element):
        currentLongest = 0
        strElement = str(element)
        for i in range(len(strElement)):
            currentItem = int(strElement[:i+1])
            if currentItem in hashSet:
                if currentLongest < len(strElement[:i+1]):
                    currentLongest = len(strElement[:i+1])
                    
        return currentLongest

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hashSet = set()
        for item in arr1:
            strItem = str(item)
            for i in range(len(strItem)):
                currentItem = int(strItem[:i+1])
                hashSet.add(currentItem)
        longest = 0
        for item in arr2:
            currentLongest = self.findLongest(hashSet, item)
            if currentLongest> longest:
                longest = currentLongest
        return longest