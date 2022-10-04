class Solution(object):
    def carFleet(self, target, position, speed):
       
        stack=[]
        positionSorted= sorted(enumerate(position), key=lambda i: i[1])
     
        for i, place in enumerate(positionSorted):
            
            time=float((target-place[1]))/float(speed[place[0]])
            
            
            while stack and stack[-1]<=time:
                stack.pop()
            stack.append(time)
        return(len(stack))
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        