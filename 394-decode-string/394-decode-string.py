class Solution(object):
    def decodeString(self, s):
        stack=[]
        for string in s:
            if string!="]":
                stack.append(string)
            else:
                multiplier=""
                tempostore=""
                while stack[-1]!="[":
                    tempostore=stack.pop()+tempostore
                stack.pop()
                while stack and stack[-1].isdigit():
                    multiplier=stack.pop()+multiplier
                stack.append(int(multiplier)*tempostore)
        return "".join(stack)
            
        """
        :type s: str
        :rtype: str
        """
        