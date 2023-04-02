class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n, lastbit = divmod(n,2)
        while n:
            n, newlast = divmod(n,2)
            if lastbit == newlast:
                return False
            lastbit = newlast
        return True
