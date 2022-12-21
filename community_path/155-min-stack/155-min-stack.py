class MinStack(object):
     
     def __init__(self):
        self.stack=[]

     def push(self, val):
        self.stack.append(val)
        """
        :type val: int
        :rtype: None
        """
        

     def pop(self):
        if(len(self.stack)!=0):
           self.stack.pop()
        """
        :rtype: None
        """
        

     def top(self):
        return self.stack[len(self.stack)-1]
        """
        :rtype: int
        """
        

     def getMin(self):
        return min(self.stack)
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()