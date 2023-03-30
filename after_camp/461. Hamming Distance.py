class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin, y_bin = bin(x), bin(y)
        point_x = len(x_bin ) - 1
        point_y = len(y_bin) - 1
        count_different = 0
        while x_bin[point_x] != "b" and y_bin[point_y] != "b":
            if x_bin[point_x] != y_bin[point_y]:
                count_different += 1
            point_x -= 1
            point_y -= 1
       
        while x_bin[point_x] != "b":
                if x_bin[point_x] == "1":
                    count_different += 1
                point_x -= 1
    
        while y_bin[point_y] != "b":
            if y_bin[point_y] == "1":
                count_different += 1
            point_y -= 1
        return count_different
