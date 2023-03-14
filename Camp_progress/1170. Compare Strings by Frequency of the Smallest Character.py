class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        output = []
        for i,string in enumerate(words):
          words[i] = string.count(min(string))
        
        words.sort()
        for string in queries:
            freq_qurie = string.count(min(string))
            l = 0
            r = len(words) - 1
            
            while l <= r:
                mid = (l + r) // 2
                if words[mid] <= freq_qurie:
                    l = mid + 1
                else:
                    r = mid - 1
            output.append(len(words)-1 -r)
        return output
