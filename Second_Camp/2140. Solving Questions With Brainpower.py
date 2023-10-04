class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dict = {}
        
        def dp(idx):
            if idx in dict:
                return dict[idx]

            if idx >= n: 
                return 0
            
            taking = questions[idx][0] + dp(idx + questions[idx][1] + 1)
            not_taking = dp(idx + 1)
            dict[idx] = max(taking, not_taking)
            return dict[idx]
        return dp(0)
            


        
