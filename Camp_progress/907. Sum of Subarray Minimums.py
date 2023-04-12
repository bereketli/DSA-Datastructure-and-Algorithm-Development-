class Solution(object):
    def sumSubarrayMins(self, arr):
        modulo = 10**9 + 7
        stack =[]
        summed =0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                 popped = stack.pop()
                 if stack :
                    prev_smaller =stack[-1]
                 else:
                    prev_smaller= -1
                    
                 summed =(summed + (popped - prev_smaller) *(i -popped ) * arr[popped]) % modulo
            stack.append(i)
        
        while stack:
                 popped = stack.pop()
                 
                 if stack :
                    prev_smaller =stack[-1]
                 else:
                    prev_smaller= -1
                    
                 summed =(summed + (popped - prev_smaller ) *(len(arr) - popped) * arr[popped]) % modulo
                
                 
        return summed
                 
            
        
        
        """
        prev_next_smaller =[[0,0],[0,3],[2,3],[3,3]]
        arr = [3,1,2,4]
        stack =[1, 2,3]
        
        
        3 + 6 + 4 + 4  = 17
         
         
        :type arr: List[int]
        :rtype: int
        """
        
