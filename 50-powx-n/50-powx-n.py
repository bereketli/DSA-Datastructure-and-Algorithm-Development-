class Solution(object):
    def myPow(self, x, n):
        if x==1 or x==-1:
            return -1 if (x==-1 and n%2!=0) else 1
        if n<-20:
                return 0
        def power(num,index):
        
            
            if index==0:
                  return 1 
            memo=power(x,index/2)
            if index%2==0:
                return memo**2
            else:
                return memo**2*num
        return power(x,n)  if(n>0) else 1/power(x,abs(n))
        
       
            
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        