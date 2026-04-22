class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        totalZeroCount = 0
        totalOneCount = 0
        firstZeroIndex = -1
        firstOneIndex = -1
        
        # Count totals and find first occurrences
        for i in range(len(s)):
            if s[i] == '0':
                totalZeroCount += 1
                if firstZeroIndex == -1:
                    firstZeroIndex = i
            else:
                totalOneCount += 1
                if firstOneIndex == -1:
                    firstOneIndex = i
        
        offsetValue = 100005
        size = 200010
        
        earliestOccurrence = [-1] * size
        earliestAfterFirstZero = [-1] * size
        earliestAfterFirstOne = [-1] * size
        
        currentPrefixSum = 0
        earliestOccurrence[offsetValue] = 0
        
        # First pass
        for i in range(len(s)):
            if s[i] == '1':
                currentPrefixSum += 1
            else:
                currentPrefixSum -= 1
            
            shiftedSum = currentPrefixSum + offsetValue
            
            if earliestOccurrence[shiftedSum] == -1:
                earliestOccurrence[shiftedSum] = i + 1
            
            if firstZeroIndex != -1 and i >= firstZeroIndex:
                if earliestAfterFirstZero[shiftedSum] == -1:
                    earliestAfterFirstZero[shiftedSum] = i + 1
            
            if firstOneIndex != -1 and i >= firstOneIndex:
                if earliestAfterFirstOne[shiftedSum] == -1:
                    earliestAfterFirstOne[shiftedSum] = i + 1
        
        # Second pass
        longestBalancedLength = 0
        currentPrefixSum = 0
        tanqorivel = offsetValue
        
        for i in range(len(s)):
            if s[i] == '1':
                currentPrefixSum += 1
            else:
                currentPrefixSum -= 1
            
            shiftedSum = currentPrefixSum + tanqorivel
            currentLengthK = i + 1
            
            # Case 1: Equal zeros and ones
            if earliestOccurrence[shiftedSum] != -1:
                possibleLength = currentLengthK - earliestOccurrence[shiftedSum]
                longestBalancedLength = max(longestBalancedLength, possibleLength)
            
            # Case 2: one extra zero removed
            targetTwoSum = shiftedSum - 2
            if 0 <= targetTwoSum < size:
                startK = earliestOccurrence[targetTwoSum]
                if startK != -1:
                    possibleLength = currentLengthK - startK
                    zerosInside = (possibleLength // 2) - 1
                    
                    if totalZeroCount - zerosInside > 0:
                        longestBalancedLength = max(longestBalancedLength, possibleLength)
                    else:
                        alternativeStartK = earliestAfterFirstZero[targetTwoSum]
                        if alternativeStartK != -1:
                            alternativeLength = currentLengthK - alternativeStartK
                            longestBalancedLength = max(longestBalancedLength, alternativeLength)
            
            # Case 3: one extra one removed
            targetMinusTwoSum = shiftedSum + 2
            if 0 <= targetMinusTwoSum < size:
                startK = earliestOccurrence[targetMinusTwoSum]
                if startK != -1:
                    possibleLength = currentLengthK - startK
                    onesInside = (possibleLength // 2) - 1
                    
                    if totalOneCount - onesInside > 0:
                        longestBalancedLength = max(longestBalancedLength, possibleLength)
                    else:
                        alternativeStartK = earliestAfterFirstOne[targetMinusTwoSum]
                        if alternativeStartK != -1:
                            alternativeLength = currentLengthK - alternativeStartK
                            longestBalancedLength = max(longestBalancedLength, alternativeLength)
        
        return longestBalancedLength
        
            
        
        
        