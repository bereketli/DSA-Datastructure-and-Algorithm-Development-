class Solution(object):
    def kClosest(self, points, k):
       
        output=[]
        store=[]
        for point in range(len(points)):
            distance=points[point][0]**2+points[point][1]**2
            store.append([distance,points[point]])
        store.sort()
     
        for point in range(k):
            output.append(store[point][1])
        return output
        
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        