class Solution:
    def numTrees(self, n: int) -> int:
        ans = 1
        for i in range(n+1, 2*n+1):
            ans *= i
            ans //= i - n
        return ans // (n+1)
