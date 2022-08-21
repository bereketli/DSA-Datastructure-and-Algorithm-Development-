class Solution(object):
    def isPowerOfTwo(self, n):
        if(n<=0):
            return False
        def pow_of_two(num,divisor):
          
        
            if(  num==1 or float(num)/float(divisor)==1 ):
                
                return True
            if(num<divisor):
               
                return pow_of_two(num,divisor/2)
            
            
            if(num%divisor!=0 ):
                return False
            
           
            return pow_of_two(num/divisor,divisor*2)
        return pow_of_two(abs(n),2)
        """
        :type n: int
        :rtype: bool
        """
        