class Solution(object):
    def fib(self, n):
        
         while n>=2:
           return self.fib(n-2)+self.fib(n-1)
         if(n==1):
            return 1
         if(n==0):
            return 0

      