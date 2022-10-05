class Solution(object):
    def reverseWords(self, s):
        output =""
        i ,j = 0,0
        while j < len(s):
            while i < len(s) and s[i] == " ":
                  i +=1
            j = i + 1
            while j < len(s) and s[j] != " ":
                  j +=1
            if i< len(s) and s[i] != " ":
              output = s[i:j] + " " + output if output else s[i:j] + output
           
            i = j +1
        return output
           
        """
        :type s: str
        :rtype: str
        """
        