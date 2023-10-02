class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices) 
        def dp(i, holding_stock, memo):
            if i == n:
                return 0
            if (i, holding_stock) in memo:
                return memo[(i, holding_stock)]
              
            if holding_stock:
               
                sell = dp(i + 1, False, memo) + prices[i] - fee
                no_action = dp(i + 1, True, memo)
                memo[(i, holding_stock)] = max(sell, no_action)
            else:
                
                buy = dp(i + 1, True, memo) - prices[i]
                no_action = dp(i + 1, False, memo)
                memo[(i, holding_stock)] = max(buy, no_action)
            
            return memo[(i, holding_stock)]
        return dp(0, False, {})
        
        
            
