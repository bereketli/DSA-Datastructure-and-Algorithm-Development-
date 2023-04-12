class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:  
        n = len(intervals)
        output = [-1] * n
        index = [i for i in range(n)]
        index = sorted(index, key = lambda x: intervals[x][0])
        for i in index:
            end_i = intervals[i][1]
            l = 0
            r = n -1
            while l <= r:
                mid = (l + r) // 2
                if intervals[index[mid]][0] >= end_i:
                    r = mid -1
                else:
                    l = mid + 1
            greater = index[l] if r < n -1 else -1
            output[i] = greater
        return output
        """
        sort based on the start[i]
        using binary search, find the greater start[j] than end i
        [[3,4],[2,3],[1,2]]
         0 , 1 , 2
         2, 1, 0
         T = 2


        """



                
