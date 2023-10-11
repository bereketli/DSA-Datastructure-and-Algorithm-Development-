class Solution:
    def numTeams(self, rating: List[int]) -> int:

        count = 0
        for i in range(1,len(rating)):
            countless = 0
            for j in range(i -1, -1, -1):
                if rating[j] < rating[i]:
                    countless += 1
            counthigh = 0
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    counthigh += 1
            
            if countless and counthigh:
                count += (countless * counthigh)
              
        
        for i in range(1, len(rating)):
            counthigh = 0
            for j in range(i -1, -1, -1):
                if rating[j] > rating[i]:
                    counthigh += 1
            countless = 0  
            for j in range(i + 1, len(rating)):
                if rating[j] < rating[i]:
                    countless += 1
            
            if countless and counthigh:
                count += (countless * counthigh)
        return count

        
