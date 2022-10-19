class Solution(object):
    def threeSumMulti(self, arr, target):
        arr.sort()
        modulo = 10 **9 +7
        ans =0
        for i in range(len(arr)):
            wanted = target - arr[i]
            j = i +1
            k = len(arr) -1
            while j < k:
                if j <k and arr[j] + arr[k] < wanted:
                    j +=1
                elif j < k and arr[j] + arr[k] > wanted:
                    k -=1
              
                elif arr[j] != arr[k]:
                    left = right =1
                    while j + 1 < k and arr[j] == arr[j + 1]:
                             j +=1
                             left +=1
                    while k -1 > j and arr[k] == arr[k -1]:
                             k -=1
                             right +=1
                    ans += left * right
                    ans %= modulo
                    j +=1
                    k -=1
                else:
                    ans += (k - j) * (k -j +1) /2
                    ans %= modulo
                    break
              
               
        return ans
                    
                    
            
                    
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        