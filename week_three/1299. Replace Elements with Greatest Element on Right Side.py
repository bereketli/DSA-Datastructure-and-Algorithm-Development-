class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = [-1]
        maximum = arr[len(arr) -1]
        for i in range(len(arr) -2, -1, -1):
            output.append(maximum)
            maximum = max(maximum, arr[i])
            
        output.reverse()
        return output
