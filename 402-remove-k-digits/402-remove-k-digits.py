class Solution(object):
    def removeKdigits(self, num, k):
        if len(num)==k:
            return "0"
        else:
            mono_stack=[]
            removed=0
            for i in range(len(num)):
               while mono_stack and removed<k and num[i]<mono_stack[-1]:
                   
                   mono_stack.pop()
                   removed+=1
               mono_stack.append(num[i])
            if removed<k:
            
                return str(int("".join(mono_stack[:len(mono_stack)-(k-removed)])))
                
            else:
                 return str(int("".join(mono_stack)))
               
                
        
        
        
        
        
        
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        