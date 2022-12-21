class Solution(object):
    def validateStackSequences(self, pushed, popped):
        
        
        stack = []
        top = -1
        m=0
        for i in range(len(popped)):
            if(top>=0 and popped[i]==stack[top]): 
                  
                    stack.pop()
                    top-=1
                    continue
            for j in range(m, len(pushed)):
                if( pushed[j]!=popped[i]):
                    stack.append(pushed[j])
         
                    top+=1
       
                    m=j+1
          
                if(pushed[j]==popped[i]):
                    m+=1

           
                    break

            
         
        
            
            if(top>=0 and popped[i]==stack[top]): 
                stack.pop()
                top-=1
                  
                    
                   
        
        if (len(stack)==0):
            return True
        
       
        
       
  
        