class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        return [s for s in queries if any(deque(takewhile(lambda p:p<4,
            accumulate(map(ne,s,t))),maxlen=1)[0]<3 for t in dictionary)]