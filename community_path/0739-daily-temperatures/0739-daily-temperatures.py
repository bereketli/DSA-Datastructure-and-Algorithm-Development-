class Solution(object):
    def dailyTemperatures(self, temperatures):
         answer =[0] * len(temperatures)
         dec_stack =[]
         for i in range(len(temperatures)):
                while dec_stack and temperatures[dec_stack[-1]] < temperatures[i]:
                    popped = dec_stack.pop()
                    answer[popped] = i - popped
                dec_stack.append(i)
                
         return answer