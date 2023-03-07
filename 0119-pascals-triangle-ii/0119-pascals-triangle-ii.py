class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(n):
            if n == 0:
                return [1]
            previous = pascal(n - 1)
            arr = [1]
            for i in range(len(previous) -1):
                arr.append(previous[i] + previous[i + 1])
            arr.append(1)
            return arr
        return pascal(rowIndex)
        