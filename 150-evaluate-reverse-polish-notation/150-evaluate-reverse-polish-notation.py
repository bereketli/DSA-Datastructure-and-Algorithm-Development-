class Solution(object):
    import math
    def evalRPN(self, tokens):
      
        stack=[]
        top=-1
        for token in tokens:
          
            if(token=='+' or token=='-' or token=='*' or token=='/'):
                if(token=='+'):
                    result= (int(stack[top-1]) + int(stack[top]))
                elif(token=='-'):
                    result= (int(stack[top-1]) - int(stack[top]))
                elif(token=='*'):
                    result=(int(stack[top-1]) *int(stack[top]))
                elif(token=='/'):
                    result= int(float(stack[top-1])/ float(stack[top]))
                stack.pop() 
                top-=1
                if(top>=0):
                    stack[top]=result
            else:
                stack.append(token)
               
                top+=1
        return stack[0]
                 
           