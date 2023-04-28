class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        que = deque([0])
        visited = set([0])
        while que:
            room = que.popleft()
            for key in rooms[room]:
                if key not in visited:
                    que.append(key)
                    visited.add(key)
        if len(visited) == len(rooms):
            return True
        else:
            return False

