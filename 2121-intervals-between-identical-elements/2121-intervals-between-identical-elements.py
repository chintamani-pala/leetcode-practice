class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        dictObj = {}
        for i in range(len(arr)):
            if arr[i] in dictObj:
                tempObj = dictObj[arr[i]]
                tempObj.append(i)
                dictObj[arr[i]] = tempObj
            else:
                dictObj[arr[i]] = [i]
        ansArr = [-1]*len(arr)
        for num, indices in dictObj.items():
            prefix = [0]*(len(indices)+1)
            for i in range(len(indices)):
                prefix[i+1] = prefix[i] + indices[i]
            for i in range(len(indices)):
                ind = indices[i]

                #left
                leftCount = i
                leftSum = prefix[i]
                left = ind * leftCount - leftSum

                #right
                rightCount = len(indices)-i-1
                rightSum = prefix[-1] - prefix[i+1]
                right = ind * rightCount - rightSum
                ansArr[ind] = abs(left) + abs(right)
        return ansArr
