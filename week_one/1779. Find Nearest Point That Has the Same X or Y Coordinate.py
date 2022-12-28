class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhata = [-1,10 ** 5]
        for i in range(len(points)):
            if x == points[i][0] and abs(y - points[i][1]) < manhata[1]:
                manhata[0] = i
                manhata[1] = abs(y - points[i][1])
            if y == points[i][1] and abs(x - points[i][0]) < manhata[1]:
                manhata[0] = i
                manhata[1] = abs(x - points[i][0])
        return manhata[0]