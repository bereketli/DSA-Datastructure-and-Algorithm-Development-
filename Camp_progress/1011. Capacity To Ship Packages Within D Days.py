class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            count_days = 1
            current_weights = 0

            # count no of days carried by mid capacity
            for i,num in enumerate(weights):

                    current_weights += num
                    if current_weights > mid:
                        count_days += 1
                        current_weights = num
                    elif i < len(weights) -1 and current_weights == mid: 
                        count_days +=  1
                        current_weights = 0
           
            if count_days <= days:
                
                right= mid - 1
            else:
                
                left = mid + 1
           
        return left
            
