class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2= Counter(s2[0:len(s1) -1])
        left, right = 0, len(s1) -1
        
        while right < len(s2):
            if s2[right] not in count_s2:
                    count_s2[s2[right] ] = 1
            else:
                    count_s2[s2[right] ] += 1
            if count_s1 == count_s2:
                return True
            if count_s2[s2[left]] == 1:
                    count_s2.pop(s2[left]) 
            else:
                    count_s2[s2[left] ] -= 1
            left += 1
            right += 1
        return False
            
            

            

                