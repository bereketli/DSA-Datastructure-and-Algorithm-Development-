class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        count=0
        left=0
        right=len(people)-1
        while right>left:
            
            if people[right]+people[left]<=limit:
              
                left+=1
            count+=1
            right-=1
            if right==left:
                    count+=1
        return count
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        