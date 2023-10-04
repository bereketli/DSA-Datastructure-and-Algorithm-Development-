import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for source, destiny, weight in times:
            graph[source].append([destiny, weight])

        def dijkstra(graph, start):
            distances = [ float("inf") for _ in range(n + 1)]
            distances[start] = 0
            visited = set()
            priority_queue = [(0, start)]

            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_node in visited:
                    continue
                visited.add(current_node)
                for neighbor, weight in graph[current_node]:

                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
        
            return max(distances[1:])
               
        mindistance = dijkstra(graph, k)
        if mindistance != float("inf"):
            return mindistance
        else:
            return -1
       
       
