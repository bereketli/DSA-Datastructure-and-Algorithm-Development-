class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        l = 0
        for r in range(1,len(prices)):
            if prices[r] <= prices[l]:
                l = r
            else:
                current_max = max(current_max, prices[r] - prices[l])

        return current_max
        Input: prices = [7,1,5,3,6,4]
        Output: 5
