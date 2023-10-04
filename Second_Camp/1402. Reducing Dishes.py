class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        i = len(satisfaction) - 1
        max_val = 0
        test, total = 0, 0
      
        
        while i >= 0:
            total += satisfaction[i]
            test += total

            if test < max_val:
                return max_val

            max_val = test
            i -= 1

        return max_val

            
