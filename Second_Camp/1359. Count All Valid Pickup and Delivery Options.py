class Solution:
    def countOrders(self, n: int) -> int:
        modu = (10**9) + 7
        previous = 1
        for i in range(2, n + 1):
            item = 2 * (i- 1) + 1
            permutate = item * (item + 1) >> 1
            previous *= permutate
            previous %= modu
        return previous


        
