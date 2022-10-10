class Solution(object):
    def isStrictlyPalindromic(self, n):
        if n == 4:
            return False
        remain =""
        remain += str(n % (n - 2) )
        
        remain =str(n //(n-2) % (n - 2)) + remain
        
        if remain != "12":
            return True
        else:
            return False
            
      
        """
        :type n: int
        :rtype: bool
        """
        