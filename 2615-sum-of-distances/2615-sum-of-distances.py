class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dictObj = {}
        for i in range(len(nums)):
            if nums[i] in dictObj:
                tempObj = dictObj[nums[i]]
                tempObj.append(i)
                dictObj[nums[i]] = tempObj
            else:
                dictObj[nums[i]] = [i]
        ansArr = [-1]*len(nums)
        for num, indices in dictObj.items():
            # tempInd = dictObj[nums[i]][:]
            # if len(tempInd)==1:
            #     continue
            # tempInd.remove(i)
            # ans = 0
            # for item in tempInd:
            #     ans += abs(i-item)
            # ansArr[i] = ans
            
            prefix = [0]*(len(indices)+1)
            for i in range(len(indices)):
                prefix[i+1] = prefix[i] + indices[i]
            
            for i in range(len(indices)):
                ind = indices[i]

                leftCount = i
                left_sum = prefix[i]
                left = ind * leftCount - left_sum

                rightCount = len(indices)-i-1
                right_sum = prefix[-1] - prefix[i+1]
                right = ind * rightCount - right_sum

                ansArr[ind] = abs(left) + abs(right) 
        return ansArr