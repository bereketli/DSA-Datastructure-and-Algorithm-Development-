class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        totalTime = 0
        for i in range(len(tickets)):
            if i <= k and tickets[k] <= tickets[i]:
                totalTime += tickets[k]
            elif i > k and tickets[k] <= tickets[i]:
                totalTime += tickets[k]- 1
            else:
                totalTime += tickets[i]
        return totalTime 
