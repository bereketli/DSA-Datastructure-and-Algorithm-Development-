class Solution(object):
    def reverseParentheses(self, s):
        i=0
        top=-1
        stack=[]
        temporary=[]
        test=True
       
       
        while test:
            
            while i<len(s) and s[i]!=')':
                stack.append(s[i])
                top+=1
                i+=1
            if i<len(s) and s[i]==")":
                while top>0 and stack[top]!='(':
                   
                    temporary.append(stack.pop())
                    top-=1
                stack.pop()
                top-=1
                   
                
                stack=stack+temporary
             
                top=len(stack)-1
                temporary=[]
         
            if i>=len(s)-1:
                test=False
            i+=1
            
       
        return "".join(stack)
           
               
               
        """
        :type s: str
        :rtype: str
        """
        