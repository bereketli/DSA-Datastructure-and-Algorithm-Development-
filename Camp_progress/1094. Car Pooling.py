class Solution(object):
    def carPooling(self, trips, capacity):
        position =[0] 
        
        for passen, init, desti in trips:
            
            if desti >= len(position):
                position += [0] * (desti - len(position) +1)
            
            position[init] +=passen
            position[desti] -= passen
        prefi =0
        for i in range(len(position)):
            prefi += position[i]
            if prefi > capacity:
                return False
        return True
            
        """
        store =[0,2,0,3,0,-2,-7]
        trips = [[2,1,5],[3,3,7]], capacity = 4
        
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
