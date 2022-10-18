class Solution(object):
    def calculate(self, s):
        currentNumber =0
        stack =[]
        operation = "+"
        s+="."
       
        for i in s:
         
            if i.isdigit():
                currentNumber = (10 * currentNumber) + int(i)
           
            elif i==" ":
                continue
            else:
                if operation =="+":
                    stack.append(currentNumber)
                elif operation =="-":
                     
                     stack.append(-currentNumber)
                elif operation == "*":
                      first = stack.pop()
                      stack.append(first * currentNumber)
                elif operation =="/":
                      first = stack.pop()
                     
                      stack.append(math.trunc(float(first )/float(currentNumber)))
                else:
                    stack.append(currentNumber)
                currentNumber =0
                operation = i
               
        return sum(stack)
                       
                      
        
        """
        :type s: str
        :rtype: int
        """
        