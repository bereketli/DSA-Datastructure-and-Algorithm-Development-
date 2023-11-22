class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(lambda: 0))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        tot = 0
        x, y = point
        for yp in self.points[x].keys():
            if yp == y:
                continue
            tot += self.points[x][yp] * (self.points[x + (y-yp)][yp] * self.points[x + (y-yp)][y] + self.points[x - (y-yp)][yp] * self.points[x - (y-yp)][y])
        return tot
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)