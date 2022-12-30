class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count ={}
        solu_first = set()
        solu_second = set()
        for match in matches:
            
            if match[1] not in count:
                count[match[1]] = 1
            else:
                count[match[1]] +=1
        for match in matches:
            if match[0] not in count:
                solu_first.add(match[0])
            if count[match[1]] == 1:
                solu_second.add(match[1])
        
        return [sorted(list(solu_first)),sorted(list(solu_second))]
            