class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.start= image[sr][sc]
        def flood(row, col, image):
            if (not(0 <= row < len(image)) or not(0 <= col < len(image[0]))) or image[row][col] != self.start or  image[row][col] == color:
                return
           
            image[row][col] = color
            
            flood(row -1, col, image)     # top
            flood(row + 1, col, image)    # bottom
            flood(row, col - 1, image)    #left
            flood(row, col + 1, image)    #rihgt
            
            return image
        flood(sr,sc,image)
        return image


        
