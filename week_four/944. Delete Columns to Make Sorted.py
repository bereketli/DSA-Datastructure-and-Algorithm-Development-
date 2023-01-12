class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            column = []
            for row in range(len(strs)):
                column.append(strs[row][col])
            if column != sorted(column):
                count += 1
        return count
