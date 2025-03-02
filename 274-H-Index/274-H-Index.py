class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cites = [0] * (n+1)
        for c in citations:
            cites[min(c,n)] += 1

        hdex = 0
        for i in range(n,-1,-1):
            hdex += cites[i]
            if hdex >= i:
                return i