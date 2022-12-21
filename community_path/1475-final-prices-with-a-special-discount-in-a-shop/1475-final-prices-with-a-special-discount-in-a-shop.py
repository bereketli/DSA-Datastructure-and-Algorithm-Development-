class Solution(object):
    def finalPrices(self, prices):
        stack=[]
        output=[0]*len(prices)
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                index=stack.pop()
                output[index]=prices[index]-prices[i]
            stack.append(i)
        while stack:
            index=stack.pop()
            output[index]=prices[index]
        return output
        
     
        