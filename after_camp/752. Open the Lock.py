from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        que = deque([["0000", 0]])
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        deadends.add("0000")
        while que:
            current, depth = que.popleft()
            if current == target:
                return depth
            
            for i in range(4):
                up = str((int(current[i]) + 1) % 10)
                down = str((int(current[i]) - 1 + 10) % 10 )
                child_up = current[:i] + up + current[i + 1:]
                child_down = current[:i] + down + current[i +1:]
                if child_up not in deadends:
                    que.append([child_up, depth + 1])
                    deadends.add(child_up)
                if child_down not in deadends:
                    que.append([child_down, depth + 1])
                    deadends.add(child_down)

        return -1

 
