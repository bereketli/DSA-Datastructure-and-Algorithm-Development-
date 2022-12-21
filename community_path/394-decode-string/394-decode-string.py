class Solution(object):
    index=0
    def decodeString(self, s):
        
        def decoded():
             num=""
             ans=""
             while self.index<len(s) and s[self.index]!="]":
                memo=""
                if s[self.index].isdigit():  #check if it is a number
                   
                    num+=s[self.index]
                    self.index+=1
                    continue
                elif s[self.index]=="[": #recall the function recursively for anew                                             bracket
                                           #and return new brackets result
                    self.index+=1
                    memo=decoded()
                 
                    self.index+=1
                else:                      #if the value is  english alphabet
                    ans+=s[self.index]
                    self.index+=1
                    continue 
                if num :                    # multiply the result
                    ans+=(memo)*int(num)
                    num=""
             return ans
        return decoded()
            
        """
        :type s: str
        :rtype: str
        """
        