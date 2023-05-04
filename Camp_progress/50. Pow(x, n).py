class Solution(object):
    def myPow(self, x, n):
        def power(num,index):
            if index==0:
                  return 1 
            tempo = power(num, index//2)
            if index%2==0:
                return tempo**2
            else:
                return tempo**2*num
        return power(x,n) 
        
       
            
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        
