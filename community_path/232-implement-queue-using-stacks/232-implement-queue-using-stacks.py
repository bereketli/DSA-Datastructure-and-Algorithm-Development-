class MyQueue(object):
    
    def __init__(self):
        self.stack=[]

    def push(self, x):
        self.stack.append(x)
      

    def pop(self):
        if(self.empty()==False):
            x=self.peek()
            self.stack.pop(0)
            return x
      

    def peek(self):
         if(self.empty()==False):
           return self.stack[0]
      

    def empty(self):
        if(len(self.stack)==0):
            return True
        else:
            return  False
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()