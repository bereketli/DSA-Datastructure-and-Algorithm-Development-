class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        sortedTasks = [[tasks[i][0], tasks[i][1], i] for i in range(n)]

        sortedTasks.sort(key=lambda x: (x[0], x[1], x[2]))

        pq = []  # Priority queue (min heap)
        time = 0
        answer = []
        i = 0
        index = 0

        while index < n or pq:
            if not pq and time < sortedTasks[index][0]:
                time = sortedTasks[index][0]

            while index < n and time >= sortedTasks[index][0]:
                heapq.heappush(pq, [sortedTasks[index][1], sortedTasks[index][2]])
                index += 1

            task = heapq.heappop(pq)
            time += task[0]
            answer.append(task[1])
            i += 1

        return answer
