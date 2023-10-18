class Solution:
    def __init__(self):
        self.list = []
        self.map = {}

    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        self.list = [list(prefs) for prefs in preferences]
        count = 0

        for i in pairs:
            self.map[i[0]] = i[1]
            self.map[i[1]] = i[0]

        for i in pairs:
            if self.isUnhappy(i[0], i[1]):
                count += 1
            if self.isUnhappy(i[1], i[0]):
                count += 1

        return count

    def isUnhappy(self, main, sub):
        subIdx = self.list[main].index(sub)
        if subIdx == 0:
            return False

        subIdx -= 1

        while subIdx >= 0:
            pat = self.list[main][subIdx]
            patPair = self.map[pat]

            pairIdx = self.list[pat].index(patPair)
            mainIdx = self.list[pat].index(main)

            if mainIdx < pairIdx:
                return True
            subIdx -= 1

        return False
