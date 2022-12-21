class Solution(object):
    def corpFlightBookings(self, bookings, n):
        flights=[0] * n 
       
        for first, last, reserve in bookings:
            flights[first -1] += reserve
            if last < n:
                flights[last] -= reserve
        answer =[flights[0]]
        for i in range(1,n):
            answer.append(answer[i -1] + flights[i])
        return answer
            
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        