class Solution(object):
    def reverseWords(self, s):
     
        arr =[]
        word =[]
        for i, char in enumerate(s):
            if not word  and char == " ":
                continue
           
            if char ==" ":
                arr.append(word)
                word = []
            else:
                word.append(char)
       
        if word:
            arr.append(word)
        l, r = 0, len(arr) - 1
        while l < r:
            arr[l] , arr[r] = arr[r], arr[l]
            l +=1
            r -=1
      
        return " ".join("".join(stri for stri in char) for char in arr)
                
        """
        :type s: str
        :rtype: str
        """
        