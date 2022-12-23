class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_dict = {}
        
        for i in range(len(order)):
            ord_dict[order[i]] = i +1
     
        for i in range(len(words) - 1):
            
            po_i , po_j = 0, 0
            while (po_i < len(words[i]) and po_j < len(words[i + 1])) and ord_dict[words[i][po_i]] == ord_dict[words[i + 1][po_j]]:
                   
                    po_i +=1
                    po_j +=1
            
            if po_j == len(words[i + 1]) and po_i < len(words[i]):
                
                return False
            elif po_j == len(words[i + 1]) and po_i == len(words[i]):
                continue
            elif po_i <len(words[i]) and po_j <len(words[i + 1]) and ord_dict[words[i][po_i]] > ord_dict[words[i +1][po_j]]:
                 return False
            
        return True