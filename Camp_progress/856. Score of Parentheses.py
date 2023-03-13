class Solution:
    def scoreOfParentheses(self, s: str) -> int:
            stack = []
            for chr in s:
                if chr == ")":
                    if stack[-1] != "(":
                        num = stack.pop()
                        stack.pop()
                        num2 = 0
                        if stack and stack[-1] != "(":
                            num2 = stack.pop()
                        stack.append(2*num + num2)
                    else:
                        num = 0
                        stack.pop()
                        if  stack and stack[-1] != "(":
                            num = stack.pop()
                        stack.append(1 + num)
                        
                else:
                    stack.append(chr)
            return sum(stack)
          
              