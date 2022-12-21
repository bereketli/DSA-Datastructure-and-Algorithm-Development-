class Solution(object):
    def minGroups(self, intervals):
        store = [0]
        for left, right in intervals:
            if right >= len(store) - 1:
                store += [0] * (right - len(store) + 2)
            store[left] +=1
            store[right + 1] -=1
        group =0
        prefi =0
        for num in store:
            prefi +=num
            group = max(group , prefi)
        return group
            
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        