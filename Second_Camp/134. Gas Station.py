class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start, idx = 0, 0
        prefix, idx = gas[idx] - cost[idx], 1
        while idx < len(gas):
            if prefix < 0:
                start = idx
                prefix = (gas[idx] - cost[idx])

            else:
                prefix += (gas[idx] - cost[idx])
            
            idx += 1
        return start

        
