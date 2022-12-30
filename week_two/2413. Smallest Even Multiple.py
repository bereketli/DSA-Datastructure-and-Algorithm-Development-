class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 2 if n % 2 != 0 else n