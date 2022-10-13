class Solution(object):
    def pancakeSort(self, arr):
        output =[]
        def fliper(index):
            l =0
            while l < index:
                arr[l], arr[index] =arr[index], arr[l]
                l +=1
                index -=1
        index= len(arr) - 1
        while index > 0:
            max_i =0
            for i in range(1,index + 1):
                if arr[max_i] < arr[i]:
                    max_i = i
            fliper(max_i)
            output.append(max_i + 1)
            fliper(index)
            output.append(index + 1)
            index -=1
        return output
            
            
                
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        