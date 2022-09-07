class Solution(object):
    def removeKdigits(self, num, k):
        if len(num)==k:
            return "0"
        else:
            mono_stack=[]
            
            for i in range(len(num)):
               while mono_stack and k and num[i]<mono_stack[-1]:
                   mono_stack.pop()
                   k-=1
               if len(mono_stack) or num[i]!='0':
                    mono_stack.append(num[i])
            
            if k:
                mono_stack=mono_stack[:-k]
            
            return "".join(mono_stack) if len(mono_stack) else "0"
               
                
        
        
        
        
        
        
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        