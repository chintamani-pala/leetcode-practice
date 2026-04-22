class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        # i  = 0
        # j = len(colors)-1
        # maximum =  0
        # while i<j:
        #     if colors[i] == colors[j]:
        #         j-=1
        #     else:
        #         maximum = max(maximum, j-i)
        #         break
        # i = 0
        # j = len(colors)-1
        # while i<j:
        #     if colors[i] == colors[j]:
        #         i+=1
        #     else:
        #         maximum = max(maximum, j-i)
        #         break
        # return maximum
        n = len(colors)-1
        for i in range(len(colors)):
            if colors[i] ^ colors[n] or colors[n-i] ^ colors[0]:
                return n-i