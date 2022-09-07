class Solution(object):
    def leastInterval(self, tasks, n):
      
        count=Counter(tasks)
        maxHeap=[-ctn for ctn in count.values()]
        heapq.heapify(maxHeap)
        performedTasks=0
        q=deque()
        while maxHeap or q:
             
              
              
              performedTasks+=1
              if maxHeap:
                   store=heapq.heappop(maxHeap)+1
                   if store:
                     q.append([store,performedTasks+n])
              if q and q[0][1]==performedTasks:
                          heapq.heappush(maxHeap,q.popleft()[0])
        return performedTasks


       
                    
    
        