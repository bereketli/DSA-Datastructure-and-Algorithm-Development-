class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = [] 
        for i in range(len(boxes)):
            summed = 0
            for j in range(len(boxes)):
                if j == i :
                    continue
                elif boxes[j] == "1":
                    summed += abs(j - i)
            output.append(summed)
        return output
                    
