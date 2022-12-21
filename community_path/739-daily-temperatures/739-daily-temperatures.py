class Solution(object):
    def dailyTemperatures(self, temperatures):
     
        output=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
                 while stack and temperatures[stack[-1]]<temperatures[i]:
                     indextop=stack[-1]
                     stack.pop()
                     output[indextop]=i-indextop
                 stack.append(i)
       
        return output
        
          