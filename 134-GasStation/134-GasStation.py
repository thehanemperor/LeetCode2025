class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fill = 0
        curr = 0
        candidate = 0
        for i in range(len(gas)):
            fill += gas[i] - cost[i]
            curr += gas[i] - cost[i]

            if curr <0:
                curr = 0
                candidate = i + 1

        return candidate if fill >=0 else -1
            
        