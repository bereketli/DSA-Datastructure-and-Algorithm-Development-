class Solution(object):
    def isPalindrome(self, s):
        
        alpha="".join(ch for ch in s if ch.isalnum())
       
        alpha=alpha.lower()
        left=0
        right=len(alpha)-1
       
        while left<right and alpha[left]==alpha[right]:
            
            left+=1
            right-=1
        if left==right or left-1==right:
            return True
        else:
            return False
        
        
        
        
        """
        :type s: str
        :rtype: bool
        """
        