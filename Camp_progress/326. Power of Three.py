class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        def power3(n):
            if n == 3 or n == 1:
                return True
            elif n < 3:
                return False
            else:
                return power3(n / 3)
        return power3(n)
        
        
            
