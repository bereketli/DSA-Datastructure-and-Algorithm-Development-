class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = [0] * 2003
        end = [0] * 2003
        
        for n in nums:
            count[n + 1000] += 1
        
        for i in range(2003):
            if count[i] < 0:
                return False
            elif i <= 2000:
                cont = min(count[i], 0 if i == 0 else end[i - 1])
                count[i] -= cont
                end[i] += cont
                count[i + 1] -= count[i]
                count[i + 2] -= count[i]
                end[i + 2] += count[i]
        
        return True
        
