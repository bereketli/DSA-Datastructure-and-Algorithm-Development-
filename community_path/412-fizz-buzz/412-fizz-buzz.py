class Solution(object):
    def fizzBuzz(self, n):
       
        store=[]
        for i in range(1,(n+1)):
            if(i%3==0 and i%5==0):
                store.append("FizzBuzz")
            elif(i%3==0):
                store.append("Fizz")
            elif(i%5==0):
                store.append("Buzz")
            else:
                store.append("{}".format(i))
        return store
        """
        :type n: int
        :rtype: List[str]
        """
        