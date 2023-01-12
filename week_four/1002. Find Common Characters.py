class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        origin = [0] * 26
        offset = 97
        for lett in words[0]:
            origin [ord(lett) - offset] += 1
        
        for i in range(1, len(words)):
            inner = [0] * 26
            for let in words[i]:
                inner [ord(let) - offset] += 1
            
            for j in range(26):
                origin[j] = min(origin[j], inner[j]) 
        output =[]
       
        for i in range(26):
            
              if origin[i] >0:
                    output.extend([chr(i + offset )] * origin[i])
        return output


