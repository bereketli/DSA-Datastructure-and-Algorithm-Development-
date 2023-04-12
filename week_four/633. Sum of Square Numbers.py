class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = []
        for i in range(c + 1):
            if i** 2 <= c:
                squares.append(i** 2)
            else:
                break
       
        left = 0
        right = len(squares) - 1
        while left <= right:
            if squares[left] + squares[right] > c:
                right -= 1
            elif squares[left] + squares[right] < c:
                left += 1
            else:
                return True
        return False

